from brownie import network
from helper_brownie import CHAINS
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

PINATA = {
    "enabled": False,
    "api_key": os.getenv(f"PINATA_API_KEY_MAIN")
    if network.show_active() in CHAINS["main"]
    else os.getenv("PINATA_API_KEY_TEST"),
    "api_secret": os.getenv(f"PINATA_API_SECRET_MAIN")
    if network.show_active() in CHAINS["main"]
    else os.getenv("PINATA_API_SECRET_TEST"),
}

OPENSEA = {
    "enabled": True,
    "main_url": "https://opensea.io/assets/{}/{}",
    "test_url": "https://testnets.opensea.io/assets/{}/{}",
}

HASHLIPS = {
    "enabled": True,
    "overwrite_img": True,
}
