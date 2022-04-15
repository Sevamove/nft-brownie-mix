"""
Collectible.sol constructor arguments.
"""
COLLECTIBLE = {
    "name": "Super Art Collection",  # <-
    "symbol": "SAC",  # <-
    "contract_URI": "",  # <-
    "royalty_receiver": "0x8626f6940e2eb28930efb4cef49b2d1f2c9c1199",  # <-
    "royalty_fraction": 250,  # e.g. 100 (1%); 1000 (10%) # <-
}

"""
Is collection considered as a single edition collection?
    - YES: SINGLE_EDITION_COLLECTION["enabled"] = True
    - NO: SINGLE_EDITION_COLLECTION["enabled"] = False
"""
SINGLE_EDITION_COLLECTION = {
    "enabled": True,  # <-
    "file_name": "image_name.png",  # Provide the literal name of the image in ./img # <-
}

"""
If SINGLE_EDITION_COLLECTION is enabled:
    AMOUNT_TO_MINT = 1

If SINGLE_EDITION_COLLECTION is disabled:
    AMOUNT_TO_MINT = 10
"""
AMOUNT_TO_MINT = 1 if SINGLE_EDITION_COLLECTION["enabled"] else 10  # <-

SPREADSHEET = {
    "enabled": False,  # <-
    "trait_types": [
        "1st trait type (eg. Sport)",  # <-
        "2nd trait type (eg. Languages)",  # <-
        "3rd trait type (eg. Zodiac sign)",  # <-
    ],  # <- # first row columns after | ID | NAME | DESCRIPTION | CREATOR | ARTIST | 1st trait type | 2nd ...
}

"""
@dev If SPREADSHEET is disabled and SINGLE_EDITION_COLLECTION is disabled:
@dev name = "Name" + f"# {_token_id}"
@dev description = "Description"
@dev creator = "Creator"
@dev artist = "Artist"

@dev If SPREADSHEET is disabled and SINGLE_EDITION_COLLECTION is enabled:
@dev name = "Name"
@dev description = "Description"
@dev creator = "Creator"
@dev artist = "Artist"

@dev If SPREADSHEET is enabled and SINGLE_EDITION_COLLECTION is enabled:
@dev name = <NAME PROVIDED IN SPREADSHEET UNDER ID 1>
@dev description = <DESCRIPTION PROVIDED IN SPREADSHEET UNDER ID 1>
@dev creator = <CREATOR PROVIDED IN SPREADSHEET UNDER ID 1>
@dev artist = <ARTIST PROVIDED IN SPREADSHEET UNDER ID 1>

@dev If SPREADSHEET is enabled and SINGLE_EDITION_COLLECTION is disabled:
@dev name = <NAME PROVIDED IN SPREADSHEET UNDER ID #>
@dev description = <DESCRIPTION PROVIDED IN SPREADSHEET UNDER ID #>
@dev creator = <CREATOR PROVIDED IN SPREADSHEET UNDER ID #>
@dev artist = <ARTIST PROVIDED IN SPREADSHEET UNDER ID #>
"""
COLLECTION = {
    "description": "This collection represents ...",  # <-
    "artwork": {
        "name": "Name" if not SPREADSHEET["enabled"] else None,  # <-
        "description": "Description" if not SPREADSHEET["enabled"] else None,  # <-
        "creator": "Creator" if not SPREADSHEET["enabled"] else None,  # <-
        "artist": "Artist" if not SPREADSHEET["enabled"] else None,  # <-
        "additional_metadata": {
            "enabled": False,  # <-
            "data": {
                "extra key 1": "value",  # any key | value
                "extra key 2": "value",  # any key | value
                # ...
            },
        },
    },
    "external_link": {
        "enabled": False,  # <-
        "base_url": "https://yourwebsite.io/",  # <-
        "url": "https://yourwebsite.io/super-art-collection/",  # <-
        "include_token_id": False,  # e.g. https://yourwebsite.io/super-art-collection/123 # <-
    },
}
