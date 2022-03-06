#!/bin/bash

#
# Run for more information:
#       $ brownie networks --help
#
# Add Polygon main network in order to deploy to Polygon blockchain and interact with it.
# ENV variables should be saved in .env file in brownie root directory.
#

# brownie networks add <environment> <id> host=<host_url> chainid=<network_chainid> name=<name> explorer=<scan_explorer> 
brownie networks add Polygon polygon host='https://polygon-mainnet.g.alchemy.com/v2/$WEB3_ALCHEMY_PROJECT_ID' chainid=137 name=Polygon explorer=https://api.polygonscan.com/api
