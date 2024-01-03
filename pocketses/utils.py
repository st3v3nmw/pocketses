"""Pocketses utilities."""
import psutil
from psutil._common import bytes2human


def cpu_stats() -> str:
    """CPU stats."""
    freq = psutil.cpu_freq()
    count = psutil.cpu_count()
    per_cpu = psutil.cpu_percent(interval=1, percpu=True)
    overall = sum(per_cpu) / count
    return (
        f"Overall: {overall:.1f}%\nPer CPU: {', '.join(map(lambda x: f'{x}%', per_cpu))}\n"
        f"Frequency: {freq.current:.1f} MHz (max: {freq.max:.1f} MHz)"
    )


def mem_stats() -> str:
    """Memory stats."""
    virtual = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return (
        f"Total: {bytes2human(virtual.total)} virtual, {bytes2human(swap.total)} swap\n"
        f"Used: {virtual.percent}% virtual, {swap.percent}% swap\n"
        f"Available: {bytes2human(virtual.available)} virtual, {bytes2human(swap.free)} swap"
    )


def net_stats() -> str:
    """Network I/O stats."""
    counters = psutil.net_io_counters()
    sent, recv = bytes2human(counters.bytes_sent), bytes2human(counters.bytes_recv)
    conns = "\n".join(
        [
            f"  {nic}: {', '.join(map(lambda addr: addr.address, addrs))}"
            for nic, addrs in psutil.net_if_addrs().items()
        ]
    )
    return f"Addresses:\n{conns}\n" f"Bytes: {sent} sent, {recv} received"
