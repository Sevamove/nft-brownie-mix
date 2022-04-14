from brownie import network, config, accounts

CHAINS = {
    "local": ["ganache-local", "development", "hardhat", "localhost"],
    "test": ["rinkeby", "kovan", "mumbai"],
    "main": ["mainnet", "polygon"],
}

BLOCK_CONFIRMATIONS: int = 1 if network.show_active() in CHAINS["local"] else 6


def is_verifiable_contract() -> bool:
    return config["networks"][network.show_active()].get("verify", False)


def get_account(index=None, id=None, wallet=None):
    """Return current user account."""
    if index and (network.show_active() in CHAINS["local"]):
        return accounts[index]
    elif network.show_active() in CHAINS["local"]:
        return accounts[0]
    elif id:
        return accounts.load(id)
    elif wallet:
        return config["wallets"][wallet]
    return accounts.add(config["wallets"][network.show_active()]["from_key"])


def get_event_value(_tx, _event_name: str, _key: str):
    return _tx.events[_event_name][_key]
