from brownie import Collectible
from helper_brownie import BLOCK_CONFIRMATIONS, CONTRACT_VERIFICATION, get_account
from scripts.collectible.config import COLLECTIBLE

from scripts.collectible.set_contract_uri import set_contract_uri
from scripts.utils.copy_images_and_metadata import copy_images_and_metadata


def main():
    deploy_nft()


def deploy_nft(
    _collection_name=COLLECTIBLE["name"],
    _collection_symbol=COLLECTIBLE["symbol"],
    _contract_URI=COLLECTIBLE["contract_URI"],
    _royalty_receiver=COLLECTIBLE["royalty_receiver"],
    _royalty_fraction=COLLECTIBLE["royalty_fraction"],
):

    deployer = get_account()

    collectible = Collectible.deploy(
        _collection_name,
        _collection_symbol,
        _contract_URI,
        _royalty_receiver,
        _royalty_fraction,
        {"from": deployer},
    )

    if CONTRACT_VERIFICATION["enabled"]:
        collectible.tx.wait(BLOCK_CONFIRMATIONS)
        Collectible.publish_source(collectible)

    copy_images_and_metadata()

    set_contract_uri(_account=deployer)

    return collectible
