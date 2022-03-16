from scripts.modify_metadata import modify_metadata
from scripts.helpful_scripts import get_account
from scripts.set_token_uri import set_token_uri
from scripts.safe_mint import safe_mint
from nft_config import (
    AMOUNT_TO_MINT,
    COLLECTION_NAME,
)
from brownie import NFT

def main():

    """
    If you are calling this function for the first time,
    be sure that you have (1) generated NFT images with hashlips_art_engine
    and validated them, (2) verified the necessary configurations in
    `scripts/helpful_scripts.py` and after that ran this commando:

        Don't forget to specify a wishful network (`development` by default).

        $ brownie run scripts/deploy_nft.py

    """

    account = get_account()
    nft = NFT[-1]
    current_token_id = nft.getTokenIds()

    bugs = []

    print(f"Currenct amount NFTs minted: {current_token_id}")

    while current_token_id < AMOUNT_TO_MINT:

        print("================================================================")
        print("                               OK                               ")
        print("================================================================")

        upcoming_token_id = nft.getTokenIds() + 1

        token_uri = modify_metadata(_token_id=upcoming_token_id)

        current_token_id = safe_mint(_account=account, _token_uri=token_uri)

        previous_token_id = current_token_id - 1

        if previous_token_id != 0:
            if not nft.tokenURI(previous_token_id).startswith("ipfs://"):

                print("==================================================================")
                print("                             DEFECT                               ")
                print("==================================================================")

                modify_metadata(_token_id=previous_token_id)
                set_token_uri(_account=account, _token_id=previous_token_id)

                print("==================================================================")
                print("                             SOLVED                               ")
                print("==================================================================")

                bugs.append(previous_token_id)

    print(f"\n- Nice job! Now you can enjoy NFT {COLLECTION_NAME} collection!")
    print(f"- New total amount NFTs minted: {current_token_id}")
    print("Bugs occured that were solved with this token IDs:\n", bugs)
