import pytest
from nft_config import ROYALTY_FEES_IN_BIPS
from web3 import Web3

@pytest.fixture
def get_sale_price():
    return Web3.toWei(32.11, "ether") # assumming in MATIC token.

@pytest.fixture
def get_royalty_amount():
    return (Web3.toWei(32.11, "ether") * ROYALTY_FEES_IN_BIPS) / 10000
