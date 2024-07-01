from web3 import Web3, HTTPProvider


class Web3Conection():
    
    rpc = {
        'eth':{
            'rpc': 'https://uk.rpc.blxrbdn.com',
            'name': 'Ethereum Mainnet',
            'currency': 'eth'
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
        # print(self.rpc)
        return Web3(Web3.HTTPProvider(self.rpc[chein_name]['rpc']))

    def get_checksum_address(self, wallet_address):
        try:
            return Web3.to_checksum_address(wallet_address)
        except:
            return 