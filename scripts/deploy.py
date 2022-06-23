from brownie import config, network, PlayToken
from web3 import Web3

from scripts.helpers import get_account

INITIAL_SUPPLY = Web3.fromWei(1000, "ether")

def deploy():
    # Get variables
    account = get_account()
    current_network = network.show_active()

    # Do the actual develoyment
    playToken = PlayToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][current_network].get("verify")
    )

    print(f"Deployed contract at {playToken.address}")
    print(f"Initial supply: {INITIAL_SUPPLY}")
    print(f"Name: {playToken.name()}")


def main():
    deploy()
