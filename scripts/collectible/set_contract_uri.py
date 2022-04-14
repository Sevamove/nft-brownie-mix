from helper_brownie import get_account
from scripts.utils.config import PATH, PINATA
from scripts.utils.helper import dump_to_json
from scripts.utils.pinata import upload_file
from scripts.collectible.config import COLLECTIBLE, CONTRACT_METADATA
from brownie import Collectible, network


def main():
    set_contract_uri()


def set_contract_uri(_account=None):
    print(f"Working on {network.show_active()}")

    account = _account if _account else get_account()

    collectible = Collectible[-1]
    contract_URI = COLLECTIBLE["contract_URI"]

    print("Setting contract URI ...")

    contract_uri_exists = (
        True
        if contract_URI.startswith("https://") or contract_URI.startswith("ipfs://")
        else False
    )

    if contract_uri_exists:
        set_contract_uri_tx = collectible.setContractURI(
            contract_URI, {"from": account}
        )
        set_contract_uri_tx.wait(1)
    else:
        contract_metadata_path = PATH["contract_metadata"] + "/collectible.json"
        contract_metadata = CONTRACT_METADATA
        # contract_metadata["fee_recipient"] = account.address

        if PINATA["enabled"]:
            contract_metadata["image"] = upload_file(PATH["collectible_logo"])
            dump_to_json(contract_metadata, contract_metadata_path)
            contract_URI = upload_file(contract_metadata_path)
        else:
            contract_metadata["image"] = "ipfs://HASH/logo.png"
            dump_to_json(contract_metadata, contract_metadata_path)
            contract_URI = "ipfs://Q1234ABC"

        set_contract_uri_tx = collectible.setContractURI(
            contract_URI, {"from": account}
        )
        set_contract_uri_tx.wait(1)

    print("Set contract URI successfully.")
