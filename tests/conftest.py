import pytest
from scripts.collectible.config import COLLECTIBLE
from web3 import Web3


@pytest.fixture
def get_sale_price():
    return Web3.toWei(32.11, "ether")  # assumming in MATIC token.


@pytest.fixture
def get_royalty_amount():
    return (Web3.toWei(32.11, "ether") * COLLECTIBLE["royalty_fraction"]) / 10000
