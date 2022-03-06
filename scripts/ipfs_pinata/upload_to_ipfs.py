from pathlib import Path
import requests

def upload_to_ipfs(filepath=None) -> str:

    """
    Install IFPS if you didn't done this yet then in a new terminal window run:
        $ ipfs daemon

    Using IPFS in order to upload our image to the internet and be able to
    get access to the image in 'decentralized' way.

    Disadvantage: the server must to be running all the time.
    That's why we also can additionally pin our NFT image and
    metadata using Pinata services.
    """

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-COOL.png" -> "0-COOL.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"ipfs://{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri

def main():
    upload_to_ipfs()
