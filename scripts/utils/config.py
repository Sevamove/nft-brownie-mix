from brownie import network
from helper_brownie import CHAINS
from scripts.collectible.config import (
    COLLECTIBLE,
    COLLECTION,
)
import os

IPFS: dict[str, bool] = {"enabled": False}

PATH: dict[str, str] = {
    "images": "./img",
    "token_metadata": f"./metadata/{network.show_active()}/tokens",
    "hashlips_images": "./hashlips_art_engine/build/images",
    "hashlips_metadata": "./hashlips_art_engine/build/json",
    "token_URIs": f"./metadata/{network.show_active()}/token_URIs",
    "contract_metadata": f"./metadata/{network.show_active()}/contract",
    "spreadsheet": "./metadata/nft-spreadsheet-data.xlsx",
    "collectible_logo": "./metadata/logo.png",
}

PINATA: dict[str, bool] = {
    "enabled": False,
    "api_key": bool(os.getenv(f"PINATA_API_KEY_MAIN"))
    if network.show_active() in CHAINS["main"]
    else bool(os.getenv("PINATA_API_KEY_TEST")),
    "api_secret": bool(os.getenv(f"PINATA_API_SECRET_MAIN"))
    if network.show_active() in CHAINS["main"]
    else bool(os.getenv("PINATA_API_SECRET_TEST")),
}

MARKETPLACE = {
    "opensea": {
        "enabled": True,
        "main_url": "https://opensea.io/assets/{}/{}",
        "test_url": "https://testnets.opensea.io/assets/{}/{}",
        "contract_metadata": {
            "name": COLLECTIBLE["name"],
            "description": COLLECTION["description"],
            "image": PATH["collectible_logo"],
            "external_link": COLLECTION["external_link"]["base_url"],
            "seller_fee_basis_points": COLLECTIBLE["royalty_fraction"],
            "fee_recipient": COLLECTIBLE["royalty_receiver"],
        },
    }
}

""" HASHLIPS
Before enabling it make sure that you have:
1. Installed the hashlips_art_engine and located in the brownie project root directory.
2. Generated images in ./nft-brownie-mix/hashlips_art_engine/build/images
For more information provide to the hashlips_art_engine docs.
"""
HASHLIPS: dict[str, bool] = {
    "enabled": False,
    "include_generated_metadata_attributes": False,
}
