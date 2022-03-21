from scripts.helpful_scripts import get_account, get_event_value
from scripts.modify_metadata import modify_metadata
from scripts.set_token_uri import set_token_uri
from scripts.deploy_nft import deploy_nft
from scripts.safe_mint import safe_mint
from nft_config import (
    AMOUNT_TO_MINT,
    COLLECTION_NAME,
    COLLECTION_SYMBOL,
)

def test_nft_brownie_ipfs_pinata_hashlips(get_sale_price, get_royalty_amount):
    """"""
    # Arrange.------------------------------------------------------------------
    account = get_account()
    nft = deploy_nft(_account=account)
    current_token_id = nft.getTokenIds()
    tx = None

    # Act.----------------------------------------------------------------------
    while current_token_id < AMOUNT_TO_MINT:

        upcoming_token_id = nft.getTokenIds() + 1

        token_uri = modify_metadata(_token_id=upcoming_token_id)

        current_token_id, tx = safe_mint(_account=account, _token_uri=token_uri)

        previous_token_id = current_token_id - 1

        if previous_token_id != 0:
            if not nft.tokenURI(previous_token_id).startswith("ipfs://"):

                modify_metadata(_token_id=previous_token_id)
                set_token_uri(_account=account, _token_id=previous_token_id)

    # Assert.-------------------------------------------------------------------
    assert nft.name() == COLLECTION_NAME
    assert nft.symbol() == COLLECTION_SYMBOL
    assert nft.getTokenIds() == AMOUNT_TO_MINT
    assert nft.getTokenIds() == current_token_id

    assert get_event_value(tx, "Minted", "_tokenId") == current_token_id
    assert get_event_value(tx, "Minted", "_beneficiary") == account.address
    assert get_event_value(tx, "Minted", "_tokenURI") == nft.tokenURI(current_token_id)
    assert get_event_value(tx, "Minted", "_minter") == account.address
    assert get_event_value(tx, "SetTokenURI", "_tokenId") == current_token_id
    assert get_event_value(tx, "SetTokenURI", "_tokenURI") == nft.tokenURI(current_token_id)

    assert nft.getContractURI().startswith("ipfs://")

    assert nft.getTokenExists(current_token_id + 1) is not True
    assert nft.getTokenExists(current_token_id) is True

    assert nft.getTokenOwner(current_token_id) == account.address

    assert nft.tokenURI(current_token_id).startswith("ipfs://")

    addr, amount = nft.royaltyInfo(current_token_id, get_sale_price)
    assert addr == account.address and amount == get_royalty_amount
