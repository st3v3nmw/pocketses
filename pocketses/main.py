import argparse

from snap_http import api
from twisted.internet import reactor, task

from pocketses.collector import collector
from pocketses.publisher import PubFactory


def main() -> None:
    snap_config = api.get_conf("pocketses").result

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        default=snap_config["publisher"]["port"],
        help="Port to run server",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=snap_config["collector"]["interval"],
        help="Interval in seconds to collect metrics",
    )
    args = parser.parse_args()

    factory = PubFactory()
    reactor.listenTCP(args.port, factory)

    collector_task = task.LoopingCall(collector, args.port)
    collector_task.start(args.interval)

    print("Starting publisher...")
    reactor.run()
