from brownie import network, accounts, config

LOCAL_NETWORKS = ("development", "local-ganache")
DECIMALS = 8
STARTING_ETHER = 1500 * 10 ** 8

def get_account():
    if network.show_active() in LOCAL_NETWORKS:
        return accounts[0]

    if network.show_active() == "kovan":
        return accounts.add(config["wallets"]["from_key"])
