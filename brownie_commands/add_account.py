import os

id_ = input("Provide new ID for your account:\n")

os.system("brownie accounts new {}".format(id_))
