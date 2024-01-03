"""Pocketses CLI."""
import argparse

from pocketses import utils


def cli():
    """Pocketses CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument("what", type=str, help="What's in Bilbo's pocketses?")
    args = parser.parse_args()

    match args.what:

        case "cpu":
            print(utils.cpu_stats())
        case "memory":
            print(utils.mem_stats())
        case "network":
            print(utils.net_stats())
        case _:
            print("wrong!")
