# NFT template

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


Go to the `hashlips_art_engine` and run the following command if you have `yarn` installed.
```bash
yarn install
```
Alternatively you can run this command if you have `node` installed.
```bash
npm install
```


4. Please read the `./hashlips_art_engine/README.md` (if you are not already familiar with that) about how to properly use the Hashlips Art Engine, how to upload the layers and how to give a __rarity weight__, how to set the edition size to the wishful amount of artworks in `./hashlips_art_engine/src/config.js` file.


5. Generate artworks:


For that, in `./hashlips_art_engine` directory, run:
```bash
npm run generate
```

Now you can view with specified amount your first generated artworks in `./hashlips_art_engine/build/images` and their metadata in `./hashlips_art_engine/build/json`. Later we will copy the content with the help of Python script in order to upload it to IPFS/Pinata.


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

_(coming soon)_

## Verify on Etherscan

`...`

## Viewing on OpenSea

`...`

## Resources

`...`

## License

This project is licensed under the [MIT license](LICENSE).
