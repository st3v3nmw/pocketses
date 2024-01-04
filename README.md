<div align="center">
    <img src="snap/gui/gollum.png" width="150" />
    <h1>Pocketses</h1>
    <i>What has it got in its pocketses, precious?!</i>
</div>

<br/>

This is a project I'm using to learn snaps, snapcraft, and landscape. It runs the following "services":

- A collector to pull CPU, memory, and network statistics from the host, and
- A publisher to push the metrics to all subscribed clients

"Topics" covered:

- [x] Python snap plugin
- [x] Interfaces
- [x] Pub/Sub with the [Twisted](https://twisted.org/) framework
- [x] Remote builds
- [x] Snap configuration
- [x] Hooks
- [x] Snapd REST API
- [ ] Installation on a virtual device with landscape

### Etymology

What's with the project's name I hear you ask? Well, I've been reading Tolkien's legendarium and naming things is hard _(sobs)_, as someone famously quipped. There's an open challenge to come up with a better name. And if it loses, what then? Well, if it loses, precious, then we eats it whole 🙂.

_Moving on swiftly..._

## Installation

### Source

A few pre-reqs, make sure the following are installed:

- [Snapcraft](https://snapcraft.io/docs/snapcraft-overview)
- [yq](https://github.com/mikefarah/yq)

Then run `git clone git@github.com:st3v3nmw/pocketses.git` to clone this repository and run `make build && make install`.

### Snap store

The version on the snap store is far behind (I disabled the automatic GitHub + Launchpad builds since we're using the super privileged `snapd-control` interface and you'll get rejections from the snap store). We're using the `snapd-control` interface to get pocketses' snap configuration.

If you'd still like to take the path less traveled by, run `sudo snap install pocketses --channel=candidate`.

## Setup

Connect the snap to the `system-observe`, `network-observe` & `snapd-control` interfaces (`sudo snap connect pocketses:<interface-name>`)

## Usage

As mentioned before, this snap has to be run as root since we need to connect to the `/run/snapd.socket` socket through the `snapd-control` interface. Yes, we should probably switch to the snapctl tool but parsing the output seems unwieldy (plus HTTP/JSON is convenient).

```console
$ sudo pocketses --help
usage: pocketses-cli [-h] [--port PORT] [--interval INTERVAL]

options:
  -h, --help           show this help message and exit
  --port PORT          Port to run server
  --interval INTERVAL  Interval in seconds to collect metrics
```

On one terminal, start pocketses:

```console
$ sudo pocketses
Collecting and sending stats...
Starting publisher...
Collecting and sending stats...
Collecting and sending stats...
```

On two separate terminals, subscribe with two clients:

```console
$ telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
{"cpu": {"count": 8, "utilization": {"overall": 34.3, "per_cpu": [27.6, 51.0, 46.9, 27.8, 28.7, 36.1, 26.3, 29.7]}, "frequency": {"current": 800.0, "max": 4800.0, "min": 400.0}}, "memory": {"virtual": {"total": "15.4G", "used": "42.3%", "available": "8.9G"}, "swap": {"total": "8.0G", "used": "2.9%", "available": "7.8G"}}, "network": {"traffic": {"sent": "1.4G", "recv": "1.9G"}, "addresses": {"lo": ["127.0.0.1"], "wlp108s0": ["192.168.0.104"], "docker0": ["172.17.0.1"], "lxdbr0": ["10.131.100.1"]}}}
{"cpu": {"count": 8, "utilization": {"overall": 14.6, "per_cpu": [14.0, 7.0, 15.8, 9.4, 12.1, 11.2, 19.2, 28.0]}, "frequency": {"current": 500.0, "max": 4800.0, "min": 400.0}}, "memory": {"virtual": {"total": "15.4G", "used": "42.1%", "available": "8.9G"}, "swap": {"total": "8.0G", "used": "2.9%", "available": "7.8G"}}, "network": {"traffic": {"sent": "1.4G", "recv": "1.9G"}, "addresses": {"lo": ["127.0.0.1"], "wlp108s0": ["192.168.0.104"], "docker0": ["172.17.0.1"], "lxdbr0": ["10.131.100.1"]}}}
```

You should see some output after the interval elapses (default interval = 60 seconds).

## Bugs/Features

1. The collector starts before the publisher (as seen in the output above)
2. Subscribed clients can "publish" and this output is echoed back too all clients (sender included lol)

## Resources

- [Create your first snap](https://ubuntu.com/tutorials/create-your-first-snap)
- [Adding Snapcraft parts](https://snapcraft.io/docs/adding-parts)
- [Snap confinement](https://snapcraft.io/docs/snap-confinement)
- [Snap commands and aliases](https://snapcraft.io/docs/commands-and-aliases)
- [The Python snap plugin](https://snapcraft.io/docs/python-plugin)
- [Python command line scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
- [Snap interface management](https://snapcraft.io/docs/interface-management)
- [Build snaps from GitHub](https://snapcraft.io/docs/build-from-github)
- [Snapcraft hook support](https://snapcraft.io/docs/snapcraft-hook-support)
- [Adding snap configuration](https://snapcraft.io/docs/adding-snap-configuration)
- [Supported snap hooks](https://snapcraft.io/docs/supported-snap-hooks)
- [Snapd REST API](https://snapcraft.io/docs/snapd-api)
- [Snapcraft.yaml reference](https://snapcraft.io/docs/snapcraft-yaml-reference)
- [Using the snapctl tool](https://snapcraft.io/docs/using-snapctl)
