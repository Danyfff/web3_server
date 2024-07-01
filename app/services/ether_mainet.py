from .conection import Web3Conection
from web3 import Web3

class EtheriumMainet(Web3Conection):
    
    token_contract = {
            'USDT': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
            'BNB': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52',
            'stETH': '0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
            'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
            }

    def __init__(self):
        super().__init__()

        self.w3 = self.connect_node('eth')

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
        
        balance_in_tokens = balance / (10 ** decimals)

        result = {
            'wallet': wallet_address,
            'name': name,
            'symbol': symbol,
            'balance': balance,
            'decimals': decimals
        }
        
        return result

eth = EtheriumMainet()

# for i in eth.token_contract:
#     print(eth.get_balance_by_token('0xbdfa4f4492dd7b7cf211209c4791af8d52bf5c50', i))