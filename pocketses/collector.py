import json
import socket

import psutil
from psutil._common import bytes2human


def collector(port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))

    stats = {}
    stats["cpu"] = cpu_stats()
    stats["memory"] = mem_stats()
    stats["network"] = net_stats()

    message = json.dumps(stats) + "\r\n"
    s.send(message.encode("utf-8"))
    s.close()


def cpu_stats() -> dict:
    freq = psutil.cpu_freq()
    count = psutil.cpu_count()
    per_cpu = psutil.cpu_percent(interval=1, percpu=True)
    return {
        "count": count,
        "utilization": {
            "overall": round(sum(per_cpu) / count, 1),
            "per_cpu": per_cpu,
        },
        "frequency": {
            "current": round(freq.current, 1),
            "max": freq.max,
            "min": freq.min,
        },
    }


def mem_stats() -> dict:
    virtual = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "virtual": {
            "total": bytes2human(virtual.total),
            "used": f"{virtual.percent}%",
            "available": bytes2human(virtual.available),
        },
        "swap": {
            "total": bytes2human(swap.total),
            "used": f"{swap.percent}%",
            "available": bytes2human(swap.free),
        },
    }


def net_stats() -> dict:
    counters = psutil.net_io_counters()
    nics = {
        nic: [addr.address for addr in addrs if addr.family == socket.AF_INET]
        for nic, addrs in psutil.net_if_addrs().items()
    }
    # remove NICs without IPv4 addresses
    nics = {nic: addrs for nic, addrs in nics.items() if len(addrs) > 0}
    return {
        "traffic": {
            "sent": bytes2human(counters.bytes_sent),
            "recv": bytes2human(counters.bytes_recv),
        },
        "addresses": nics,
    }
