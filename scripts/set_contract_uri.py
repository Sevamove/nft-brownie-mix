from scripts.ipfs_pinata.upload_to_pinata import upload_to_pinata
from scripts.helpful_scripts import (
    get_account,
    PATH,
    dump_to_json,
    CONTRACT_URI,
    UPLOAD_IPFS,
)
from brownie import NFT, network

def main():
    set_contract_uri()

def set_contract_uri(_account=None):
    print(f"Working on {network.show_active()}")

    account = _account if _account else get_account()

    nft = NFT[-1]

    print(f"Setting contractURI ...")

    contract_uri_path = PATH["contract_URI"] + "/contract_URI.json"
    contract_uri = CONTRACT_URI
    contract_uri["fee_recipient"] = account.address

    if UPLOAD_IPFS:
        contract_uri["image"] = upload_to_pinata(PATH["collection_logo"])
        dump_to_json(contract_uri, contract_uri_path)
        contract_uri_link = upload_to_pinata(contract_uri_path)
    else:
        contract_uri["image"] = "ipfs://HASH/logo.png"
        dump_to_json(contract_uri, contract_uri_path)
        contract_uri_link = "ipfs://HASH"

    set_contract_uri_tx = nft.setContractURI(
        contract_uri_link, {"from": account}
    )
    set_contract_uri_tx.wait(1)

    print(f"Set contractURI successfully.")
