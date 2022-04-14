import os

network = input("Choose network: (mainnet, rinkeby, kovan, polygon)\n")

os.system("brownie console --network {}".format(network))
