import os
import dotenv

dotenv.load_dotenv()

ENVIRONMENTS = {
    "mainnet": "Ethereum",
    "rinkeby": "Rinkeby",
    "kovan": "Kovan",
    "polygon": "Polygon",
}

IDS = {
    "mainnet": "mainnet",
    "rinkeby": "rinkeby",
    "kovan": "kovan",
    "polygon": "polygon",
}

HOSTS = {
    "mainnet": os.getenv("MAINNET_RPC_URL"),
    "rinkeby": os.getenv("RINKEBY_RPC_URL"),
    "kovan": os.getenv("KOVAN_RPC_URL"),
    "polygon": os.getenv("POLYGON_RPC_URL"),
}

CHAIN_IDS = {"mainnet": 1, "rinkeby": 4, "kovan": 42, "polygon": 137}

NAMES = ENVIRONMENTS

EXPLORERS = {
    "mainnet": "https://api.etherscan.io/api",
    "rinkeby": "https://api.etherscan.io/api",
    "kovan": "https://api.etherscan.io/api",
    "polygon": "https://api.polygonscan.com/api",
}

network = input("Choose network: (mainnet, rinkeby, kovan, polygon)\n")

os.system(
    "brownie networks add {} {} host={} chainid={} name={} explorer={}".format(
        ENVIRONMENTS[network],
        IDS[network],
        HOSTS[network],
        CHAIN_IDS[network],
        NAMES[network],
        EXPLORERS[network],
    )
)
