import argparse

from twisted.internet import reactor, task

from pocketses.collector import collector
from pocketses.publisher import PubFactory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        default=8888,
        help="Port to run server",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Interval in seconds to collect metrics",
    )
    args = parser.parse_args()

    factory = PubFactory()
    reactor.listenTCP(args.port, factory)

    collector_task = task.LoopingCall(collector, args.port)
    collector_task.start(args.interval)

    reactor.run()
