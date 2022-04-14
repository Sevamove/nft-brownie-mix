from brownie import Collectible
from helper_brownie import get_account

# import time
# import sys


def main():
    safe_mint()


def safe_mint(_account=None, _token_URI=None):
    account = _account if _account else get_account()
    collectible = Collectible[-1]

    print(f"Minting new NFT by assigning new tokenId and tokenURI ...")

    tx_safe_mint = collectible.safeMint(account, _token_URI, {"from": account})
    tx_safe_mint.wait(1)

    token_id = collectible.totalSupply()
    print(f"Minted NFT with the tokenId of {token_id} and tokenURI of {_token_URI}")

    # if collectible._exists(token_id) == False:
    #    print("------------------------NOT EXISTS------------------------")
    #    time.sleep(10)

    #    if collectible._exists(token_id) == False:
    #        print("Exiting...")
    #        sys.exit(f"Error: tokenId {token_id} does not exist.")

    return token_id, tx_safe_mint
