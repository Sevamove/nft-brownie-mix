# NFT template

<br/>
<p align="center">
<a href="https://webdriedesign.nl" target="_blank">
<img src="./wdd.png" width="225" alt="WebDrieDesign white logo">
</a>
</p>
<br/>

## Technology Stack & Tools

- [Solidity](https://docs.soliditylang.org/en/latest/index.html) (High-level language for implementing smart contracts)
- [OpenZeppelin](https://docs.openzeppelin.com/contracts/4.x/) (A library for secure smart contract development)
- [Brownie](https://eth-brownie.readthedocs.io/en/stable/toctree.html#) (Python development framework for Ethereum)
- [Pinata](https://docs.pinata.cloud/) (Cloud-based InterPlanetary File System service provider; no need to run IPFS node by yourself)
- [Hashlips Art Engine](https://github.com/HashLips/hashlips_art_engine) (Javascript based library that generates artworks based on provided layers)
- [Ganache](https://www.trufflesuite.com/ganache) (Local Blockchain environment)
- [Infura](https://docs.infura.io/infura/) (Blockchain API to connect to a Testnet or a Mainnet; no need to run own Blockchain node)
- [Alchemy](https://docs.alchemy.com/alchemy/) (Blockchain API to connect to a Testnet or a Mainnet; no need to run own Blockchain node)

## Requirements For Initial Setup
Please install or have installed the following:

- [NodeJS and NPM](https://nodejs.org/en/download/)
- [Python](https://www.python.org/downloads/)


## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.


```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip3
```bash
pip3 install eth-brownie
```

2. Download the repository


If you are cloning the project then run this first, otherwise you can download the source code on the release page and skip this step. 


```bash
git clone https://github.com/vsevdrob/nft-brownie-ipfs-pinata-hashlips
cd nft-brownie-ipfs-pinata-hashlips
```


3. Install Hashlips Art Engine dependencies:


Go to the `./hashlips_art_engine` and run the following command if you have `yarn` installed.
```bash
yarn install
```
Alternatively you can run this command if you have `node` installed.
```bash
npm install
```


## Testnet Development
If you want to be able to deploy to testnets, do the following.

Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html).

You can get a `WEB3_INFURA_PROJECT_ID` by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura with brownie. If you get lost, you can [follow this guide](https://ethereumico.io/knowledge-base/infura-api-key-guide/) to getting a project key. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/).

If you want to auto-upload to pinata instead of IPFS automatically, you can do so by getting a [Pinata API Key.](https://pinata.cloud/documentation#GettingStarted)

You can add your environment variables to a `.env` file. You can use the [.env.example](https://github.com/vsevdrob/nft-brownie-ipfs-pinata-hashlips/.env.example) as a template, just fill in the values and rename it to `.env`.

Here is what your `.env` should look like:
```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
export PINATA_API_KEY_TEST=<API_KEY>
export PINATA_API_SECRET_TEST=<API_SECRET>
```

You can also [learn how to set environment variables easier](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)

Then, make sure your `brownie-config.yaml` has:

```
dotenv: .env
```

![WARNING](https://via.placeholder.com/15/f03c15/000000?text=+) **WARNING** ![WARNING](https://via.placeholder.com/15/f03c15/000000?text=+)

DO NOT SEND YOUR PRIVATE KEY WITH FUNDS IN IT ONTO GITHUB

Otherwise, you can build, test, and deploy on your local environment.


You'll also need testnet rinkeby ETH. You can get ETH into your wallet by using the [rinkeby faucets located here](https://faucets.chain.link/rinkeby). If you're new to this, [watch this video.](https://www.youtube.com/watch?v=P7FX_1PePX0)


## Local Development

For local testing [install ganache-cli](https://www.npmjs.com/package/ganache-cli)
```bash
npm install -g ganache-cli
```
or
```bash
yarn add global ganache-cli
```

All the scripts are designed to work locally or on a testnet. You can add a ganache-cli or ganache UI chain like so:
```
brownie networks add Ethereum ganache host=http://localhost:8545 chainid=1337
```
And update the brownie config accordingly.


## Usage


1. Add layer folders to `hashlips_art_engine/layers/`. Then make sure that you have set the wishful edition size in `hashlips_art_engine/src/config.js` and followed the instructions about the proper setup of the layers order.

> If you are not already familiar with Hashlips Art Engine, then first you want to read the `./hashlips_art_engine/README.md` about how to properly use this program, how to set the layer folders in the right way and how to give the __rarity weight__ to each layer, how to set the edition size to the wishful amount of artworks in `./hashlips_art_engine/src/config.js` file.


2. Generate artworks:


For that, in `./hashlips_art_engine` directory, execute:
```bash
npm run generate
```

Now you can view with specified amount your first generated artworks in `./hashlips_art_engine/build/images` and their original metadata in `./hashlips_art_engine/build/json`.


3. Go to `nft_config.py` and provide some information about your collection by replacing the values in this variables:

```python
COLLECTION_NAME = "Your Collection's Name" # Change the name for each new collection.
COLLECTION_SYMBOL = "ABC" # Change the value for each new collection.
COLLECTION_DESCRIPTION = "Your Collection's Description" # What your collection is about.
AMOUNT_TO_MINT = 3 # Make sure you have enough images.

ALTERNATIVE_DATA = {
    "name": "Creative Name", # Change the name.
    "description": "The most affair description" # Change the description.
}

ADDITIONAL_METADATA = {} # {"creator": "John Doe", "artist": "John Doe"}

SPREADSHEET = {
    "enable": True,
    "include_hashlips_generated_metadata_attributes": False, # Can ignore if didn't use hashlips_art_engine
    "path": "./nft-spreadsheet-data.xlsx",
    "trait_types": ["Sport", "Languages", "Zodiac sign", "Character", "Location"],
}

NFT_EXTERNAL_LINK = {
    "enable": True,
    "root": "https://yourwebsite.io/",
    "url": "https://yourwebsite.io/your-collection/",
    "token_id": False, # https://yourwebsite.io/assets/123
}

ROYALTY_FEES_IN_BIPS = 1000 # Indicates a 10% seller fee.
```


4. Deploy NFT.sol smart contract:

```bash
brownie run scripts/01_deploy_nft.py
```


5. Mint NFTs:

```bash
brownie run scripts/02_main.py
```


After that you'll be able to view your NFTs on major marketplaces like OpenSea 🥳


## Resources

To get started with Brownie:

* Check out the [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* Check out the [Chainlink documentation](https://docs.chain.link/docs) to get started from any level of smart contract engineering. 
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* Cognitive [Brownie tutorial](https://github.com/curvefi/brownie-tutorial) by Curve Finance.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).

## License

This project is licensed under the [MIT license](LICENSE).
