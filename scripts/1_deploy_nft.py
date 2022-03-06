from scripts.copy_images_and_metadata import copy_images_and_metadata
from scripts.set_contract_uri import set_contract_uri
from brownie import NFT, network, config
from scripts.helpful_scripts import (
    get_account,
    COLLECTION_NAME,
    COLLECTION_SYMBOL,
    ROYALTY_FEES_IN_BIPS,
)

def main():
    deploy_nft()

def deploy_nft(
    _account=None,
    _collection_name=COLLECTION_NAME,
    _collection_symbol=COLLECTION_SYMBOL,
    _royalty_fees=ROYALTY_FEES_IN_BIPS,
):

    account = _account if _account else get_account()

    nft = NFT.deploy(
        _collection_name,
        _collection_symbol,
        _royalty_fees,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify", False
        )
    )

    copy_images_and_metadata()

    set_contract_uri(_account=account)

    return nft
