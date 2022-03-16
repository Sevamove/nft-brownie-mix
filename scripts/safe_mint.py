from scripts.helpful_scripts import get_account
from brownie import NFT
import time
import sys

def main():
    safe_mint()

def safe_mint(_account=None, _token_uri=None):
    account = _account if _account else get_account()
    nft = NFT[-1]

    print(f"Minting new NFT by assigning new tokenId and tokenURI ...")

    tx_safe_mint = nft.safeMint(account, _token_uri, {"from": account})
    tx_safe_mint.wait(1)

    token_id = nft.getTokenIds()
    print(f"Minted NFT with the tokenId of {token_id} and tokenURI of {_token_uri}")

    if nft.getTokenExists(token_id) == False:
        print("------------------------NOT EXISTS------------------------")
        time.sleep(10)

        if nft.getTokenExists(token_id) == False:
            print("Exiting...")
            sys.exit(f"Error: tokenId {token_id} does not exist.")

    return token_id
