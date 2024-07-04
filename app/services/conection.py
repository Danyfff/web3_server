from web3 import Web3, HTTPProvider


class Web3Conection():
    
    rpc = {
        'eth':{
            'rpc': 'https://uk.rpc.blxrbdn.com',
            'token_contracts': {
                'USDT': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
                'BNB': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52',
                'stETH': '0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
                'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
                }
            },
        'arbitrum_one':{
            'rpc': 'https://bsc-rpc.publicnode.com',
            'name': 'Arbitrum One',
            'currency': 'eth'
            },
        'arbitrum_nova':{
            'rpc': 'https://arbitrum-nova-rpc.publicnode.com',
            'name': 'Arbitrum Nova',
            'currency': 'eth'
            },
        'base':{
            'rpc': 'https://base-rpc.publicnode.com',
            'name': 'Base',
            'currency': 'eth'
            },
        'polygon':{
            'rpc': 'https://polygon-bor-rpc.publicnode.com',
            'name': 'Polygon Mainnet',
            'currency': 'matic'
            },
        'optimism':{
            'rpc': 'https://op-pokt.nodies.app',
            'name': 'OP Mainnet',
            'currency': 'eth'
            },
        'linea':{
            'rpc': 'https://linea.decubate.com',
            'name': 'Linea',
            'currency': 'eth'
            }
        }
    
    def connect_node(self, chein_name: str):
        w3 = Web3(Web3.HTTPProvider(self.rpc[chein_name]['rpc']))
        if w3.is_connected():
            print(f"Connected to {chein_name} node")
        else:
            print("Connection failed")
        return w3

    def get_checksum_address(self, wallet_address):
        try:
            return Web3.to_checksum_address(wallet_address)
        except:
            return 