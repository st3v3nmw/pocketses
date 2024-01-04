# pocketses

> What has it got in its pocketses, precious?!

Learning about Snaps &amp; Snapcraft

## Usage

- `sudo snap install pocketses --channel=candidate`: Install the snap from the snap store
- Connect the snap to the `system-observe` & `network-observe` interfaces (`sudo snap connect pocketses:<interface-name>`)

## Development

Make sure the following are installed:

- [Snapcraft](https://snapcraft.io/docs/snapcraft-overview)
- [yq](https://github.com/mikefarah/yq)

- `make build`: Build the local snap
- `make install`: Install the snap you just built

## Resources

- [Create your first snap](https://ubuntu.com/tutorials/create-your-first-snap)
- [Snap confinement](https://snapcraft.io/docs/snap-confinement)
- [Snap commands and aliases](https://snapcraft.io/docs/commands-and-aliases)
- [The python snap plugin](https://snapcraft.io/docs/python-plugin)
- [Python command line scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
- [Snap interface management](https://snapcraft.io/docs/interface-management)
- [Build snaps from GitHub](https://snapcraft.io/docs/build-from-github)
