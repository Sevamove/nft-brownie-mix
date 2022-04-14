import os

network = input("Choose network to delete: (mainnet, rinkeby, kovan, polygon)\n")

os.system("brownie networks delete {}".format(network))
