import requests
from django.apps import AppConfig
from django.conf import settings
from urllib3.exceptions import NewConnectionError
from web3 import Web3, IPCProvider


def init_wallet():
    eth_acc_id = 0
    eth_pwd = settings.ETHEREUM_ACCOUNTS[eth_acc_id]

    try:
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        acc_obj = web3.eth.accounts[eth_acc_id]
        web3.personal.unlockAccount(acc_obj, eth_pwd)
        return web3
    except requests.exceptions.ConnectionError:
        return "Fail"


class FaucetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faucet'

    def ready(self):
        self.web3 = "" #init_wallet()
        #import ui.signals


