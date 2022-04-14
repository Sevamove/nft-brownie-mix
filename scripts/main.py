from scripts.utils.modify_metadata import modify_metadata
from helper_brownie import get_account
from scripts.collectible.safe_mint import safe_mint
from scripts.collectible.config import AMOUNT_TO_MINT, COLLECTIBLE
from brownie import Collectible


def main():
    account = get_account()
    collectible = Collectible[-1]
    current_token_id = collectible.totalSupply()
    tx = None

    print(f"Currenct amount NFTs minted: {current_token_id}")

    while current_token_id < AMOUNT_TO_MINT:

        print("================================================================")
        print("                               OK                               ")
        print("================================================================")

        upcoming_token_id = collectible.totalSupply() + 1

        token_URI = modify_metadata(_token_id=upcoming_token_id)

        current_token_id, tx = safe_mint(_account=account, _token_URI=token_URI)

    print(f"\n- Nice job! Now you can enjoy NFT {COLLECTIBLE['name']} collection!")
    print(f"- New total amount NFTs minted: {current_token_id}")
