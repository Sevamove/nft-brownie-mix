from brownie import Collectible, network
from helper_brownie import CHAINS, get_account
from scripts.utils.helper import load_from_json
from scripts.utils.config import MARKETPLACE, PATH


def main():
    set_token_uri()


def set_token_uri(_account=None, _token_id=None):
    print(f"Working on {network.show_active()}")

    account = _account if _account else get_account()

    collectible = Collectible[-1]

    if not collectible.tokenURI(_token_id).startswith("ipfs://"):

        print(f"Setting tokenURI to tokenId {_token_id}")

        token_uri_path = PATH["token_URIs"] + f"/{_token_id}.json"
        token_uri = load_from_json(token_uri_path)[str(_token_id)]

        set_token_uri_tx = collectible.setTokenURI(
            _token_id, token_uri, {"from": account}
        )
        set_token_uri_tx.wait(1)

        print(f"Set tokenURI to tokenId {_token_id}")
        _show_msg(collectible, _token_id)

        return True

    else:
        print("Failed to set tokenURI. Seems it's already exist.")
        return False


def _show_msg(_collectible, _token_id):
    msg = "Awesome! You can view your NFT at"

    if MARKETPLACE["opensea"]["enabled"]:
        if network.show_active() not in CHAINS["main"]:
            print(
                msg,
                f"{MARKETPLACE['opensea']['test_url']}".format(
                    _collectible.address, _token_id
                ),
            )
        else:
            print(
                msg,
                f"{MARKETPLACE['opensea']['main_url']}".format(
                    _collectible.address, _token_id
                ),
            )

        print("Please wait up to 20 minutes, and hit the refresh metadata button")
