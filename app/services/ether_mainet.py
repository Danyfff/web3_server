from .conection import Web3Conection
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

class EtheriumMainet(Web3Conection):

    def __init__(self):
        super().__init__()

        self.w3 = self.connect_node('eth')
        self.token_contract = self.rpc['eth']['token_contracts']

    def get_gas_price(self):
        '''Получение цены на газ'''
        return self.w3.eth.gas_price
    
    def get_balance(self, wallet):
        checksum_address = self.get_checksum_address(wallet)
        balance_in_wei = self.w3.eth.get_balance(checksum_address)
        balance_in_eth = self.w3.from_wei(balance_in_wei, 'ether')
        return balance_in_eth
    
    def get_balance_by_token(self, wallet: str, token: str):
        
        token_abi = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "decimals",
            "outputs": [{"name": "", "type": "uint8"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "symbol",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "name",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
        ]

        wallet_address = self.get_checksum_address(wallet)
        contract_address = self.get_checksum_address(self.token_contract[token])
        token_contract = self.w3.eth.contract(address=contract_address, abi=token_abi)
        
        name = token_contract.functions.name().call()
        symbol = token_contract.functions.symbol().call()
        balance = token_contract.functions.balanceOf(wallet_address).call()
        decimals = token_contract.functions.decimals().call()

        result = {
            'name': name,
            'symbol': symbol,
            'balance': balance,
            'decimals': decimals
        }

        return result
    
    def get_balance_by_eth_tokens(self, wallet: str):
        result = {'wallet': wallet}
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_token = {
                executor.submit(lambda wallet, token=token: self.get_balance_by_token(wallet, token), wallet): token
                for token in self.rpc['eth']['token_contracts']
            }

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    token_balance = future.result()
                    result[token] = token_balance
                except Exception as exc:
                    print(f"{token} generated an exception: {exc}")

        result_json = json.dumps(result)

        return result
            

eth = EtheriumMainet()