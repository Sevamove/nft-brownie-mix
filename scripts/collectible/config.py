from scripts.utils.config import PATH

COLLECTIBLE = {
    "name": "Super Art Collection",
    "symbol": "SAC",
    "contract_URI": "https://",
    "royalty_receiver": "0x8626f6940e2eb28930efb4cef49b2d1f2c9c1199",
    "royalty_fraction": 250,  # e.g. 100 (1%); 1000 (10%)
}

COLLECTION_DESCRIPTION = (
    "Your Collection's Description"  # What your collection is about.
)

AMOUNT_TO_MINT = 3  # Make sure you have enough images in ./img

ALTERNATIVE_DATA = {
    "name": "Creative Name",  # Change the name.
    "description": "The most affair description",  # Change the description.
}

ALTERNATIVE_IMAGE = {
    "file_name": "image_name.png"  # Provide the literal name of the image in ./img
}

ADDITIONAL_METADATA = {
    "enabled": False,
    "creator": "John van Doe",
    "artist": "John Doe",
}  # {"creator": "John Doe", "artist": "John Doe"}

SPREADSHEET = {
    "enabled": False,
    "include_hashlips_generated_metadata_attributes": False,  # Can ignore if didn't use hashlips_art_engine
    "trait_types": ["Sport", "Languages", "Zodiac sign", "Character", "Location"],
}

NFT_EXTERNAL_LINK = {
    "enabled": False,
    "base_url": "https://yourwebsite.io/",
    "url": "https://yourwebsite.io/super-art-collection/",
    "include_token_id": False,  # https://yourwebsite.io/super-art-collection/123
}

# This contract level metadata is used
# to recieve royalty fees and is readed usually by OpenSea.
CONTRACT_METADATA = {
    "name": COLLECTIBLE["name"],
    "description": COLLECTION_DESCRIPTION,
    "image": PATH["collectible_logo"],
    "external_link": NFT_EXTERNAL_LINK["base_url"],
    "seller_fee_basis_points": COLLECTIBLE["royalty_fraction"],
    "fee_recipient": COLLECTIBLE["royalty_receiver"],
}
