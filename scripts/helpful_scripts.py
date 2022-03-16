from brownie import accounts, config, network
import json
import os

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
TESTNET_BLOCKCHAIN_ENVIRONMENTS = ["rinkeby", "kovan"]
MAIN_BLOCKCHAIN_ENVIRONMENTS = ["polygon"]

TESTNETS_OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
OPENSEA_URL = "https://opensea.io/assets/{}/{}"

def get_account(index=None, id=None, wallet=None):
    """Return current user account."""
    if index and (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[index]
    elif network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    elif id:
        return accounts.load(id)
    elif wallet:
        return config["wallets"][wallet]
    return accounts.add(config["wallets"][network.show_active()]["from_key"])

def dump_to_json(_data:dict, _pathToFile:str, _indent:int=4):
    """Dump data to *.json file."""
    with open(_pathToFile, "w") as file:
        json.dump(_data, file, indent=_indent)

def load_from_json(_pathToFile:str) -> dict:
    """Return loaded data from *.json file."""
    if os.path.exists(_pathToFile) == False:
        dump_to_json({}, _pathToFile)

    with open(_pathToFile, "r+") as file:
        data = json.load(file)
    return data
