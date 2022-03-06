from brownie import NFT, accounts, config, network
import json
import os

################################################################################
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
MAIN_BLOCKCHAIN_ENVIRONMENTS = ["polygon"]
TESTNET_BLOCKCHAIN_ENVIRONMENTS = ["rinkeby", "kovan"]
TESTNETS_OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
OPENSEA_URL = "https://opensea.io/assets/{}/{}"
################################################################################

COLLECTION_NAME = "Your Collection's Name" # Change the name for each new collection.
COLLECTION_SYMBOL = "ABC" # Change the value for each new collection.
COLLECTION_DESCRIPTION = "Your Collection's Description" # What your collection is about.
AMOUNT_TO_MINT = 3 # Make sure you have enough images.

"""
Implemented if SPREADSHEET is disabled.
Convinient if a collection that consistis of rational many images by which means
there is posibility that no unique name or description for each work of art
provided within the SPREADSHEET.
"""
ALTERNATIVE_DATA = {
    "name": "Creative Name", # Change the name.
    "description": "The most affair description" # Change the description.
}

"""
Downloads images to IPFS by using Pinata services.
If you don't want use Pinata, you can simply uncomment the function 'upload_to_ipfs'
in modify_metadata.py and comment 'upload_to_pinata'. Don't forget to activate
`ipfs daemon` in a new terminal window.
Before enabling it make sure that you have this environment variables
in your .env file:
(1st option)

    export PINATA_API_KEY=123YoUrKeyHerE
    export PINATA_API_SECRET=123YouRSecRetHere

I am using 2 different Pinata's because of separation between testing and production procedure.
Sometimes it is usefull to test out all functions using not original (Mock) images.
Don't forget to replace <COLLECTION_SYMBOL> with the value from COLLECTION_SYMBOL:
(2nd option)

    export PINATA_API_KEY_<COLLECTION_SYMBOL>=123YoUrKeyHerE
    export PINATA_API_SECRET_<COLLECTION_SYMBOL>=123YouRSecRetHere

    export PINATA_API_KEY_TEST=0123YoUrKeyHerE
    export PINATA_API_SECRET_TEST=0123YouRSecRetHere

You may stick with just 1 Pinata as the 1st option describes.
For that uncomment another 2 variabls and comment this 2.
"""
UPLOAD_IPFS = True if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS else False
PINATA_API_KEY = os.getenv(f"PINATA_API_KEY_MAIN_{COLLECTION_SYMBOL}") if network.show_active() in MAIN_BLOCKCHAIN_ENVIRONMENTS else os.getenv("PINATA_API_KEY_TEST")
PINATA_API_SECRET = os.getenv(f"PINATA_API_SECRET_{COLLECTION_SYMBOL}") if network.show_active() in MAIN_BLOCKCHAIN_ENVIRONMENTS else os.getenv("PINATA_API_SECRET_TEST")
#PINATA_API_KEY = os.getenv(f"PINATA_API_KEY")
#PINATA_API_SECRET = os.getenv(f"PINATA_API_SECRET")

"""
Adds additional key/value pair to each metadata.
"""
ADDITIONAL_METADATA = {"creator": "John van Doe", "artist": "John Doe"} # {"creator": "John Doe", "artist": "John Doe"}

"""
Before changing a path value make sure you have the directories.
"""
PATH = {
    "images": "./img",
    "metadata": f"./metadata/{network.show_active()}/metadata",
    "hashlips_images": "./hashlips_art_engine/build/images",
    "hashlips_metadata": "./hashlips_art_engine/build/json",
    "token_URIs": f"./metadata/{network.show_active()}/token_URIs",
    "contract_URI": f"./metadata/{network.show_active()}/contract_URI",
    "spreadsheet": "./metadata/nft-spreadsheet-data.xlsx",
    "collection_logo": "./metadata/logo.png"
}

"""
The first 3 columns in the first row should be: ID, Name, Description
trait_types key values are gonnna be added to the metadata (OpenSea properties).
"""
SPREADSHEET = {
    "enable": True,
    "include_hashlips_generated_metadata_attributes": False, # Can ignore if didn't use hashlips_art_engine
    "path": "./nft-spreadsheet-data.xlsx",
    "trait_types": ["Sport", "Languages", "Zodiac sign", "Character", "Location"],
}

"""
If enabled this url will be shown in each metadata, so it can provide the user
with a link for more information about your collection or work of art.
"""
NFT_EXTERNAL_LINK = {
    "enable": True,
    "root": "https://yourwebsite.io/",
    "url": "https://yourwebsite.io/your-collection/",
    "token_id": False, # https://yourwebsite.io/assets/123
}

ROYALTY_FEES_IN_BIPS = 1000 # Indicates a 10% seller fee.

# This contract level metadata will be used
# to recieve royalty fees and is readed usually by OpenSea.

CONTRACT_URI = {
    "name": COLLECTION_NAME,
    "description": COLLECTION_DESCRIPTION,
    "image": PATH["collection_logo"],
    "external_link": NFT_EXTERNAL_LINK["root"],
    "seller_fee_basis_points": ROYALTY_FEES_IN_BIPS,
    "fee_recipient": "" # Assigned in set_contract_uri.py
}

################################################################################
################################################################################

def get_account(index=None, id=None, wallet=None):
    """Return current user account."""
    if index and (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[index]
    elif network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    elif id:
        return accounts.load(id)
    elif wallet:
        return config["wallets"][wallet]
    return accounts.add(config["wallets"][network.show_active()]["from_key"])

def dump_to_json(_data:dict, _pathToFile:str, _indent:int=4):
    """Dump data to *.json file."""
    with open(_pathToFile, "w") as file:
        json.dump(_data, file, indent=_indent)

def load_from_json(_pathToFile:str) -> dict:
    """Return loaded data from *.json file."""
    if os.path.exists(_pathToFile) == False:
        dump_to_json({}, _pathToFile)

    with open(_pathToFile, "r+") as file:
        data = json.load(file)
    return data
