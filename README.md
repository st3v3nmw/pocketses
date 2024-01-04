<div align="center">
    <img src="snap/gui/gollum.png" width="150" />
    <h1>Pocketses</h1>
</div>

> What has it got in its pocketses, precious?!

Learning about Snaps &amp; Snapcraft

[![pocketses](https://snapcraft.io/pocketses/badge.svg)](https://snapcraft.io/pocketses)

## Usage

- `sudo snap install pocketses --channel=candidate`: Install the snap from the snap store
- Connect the snap to the `system-observe` & `network-observe` interfaces (`sudo snap connect pocketses:<interface-name>`)

## Development

Make sure the following are installed:

- [Snapcraft](https://snapcraft.io/docs/snapcraft-overview)
- [yq](https://github.com/mikefarah/yq)

Run:

- `make build`: to build the local snap
- `make install`: to install the snap you just built

## Resources

- [Create your first snap](https://ubuntu.com/tutorials/create-your-first-snap)
- [Adding Snapcraft parts](https://snapcraft.io/docs/adding-parts)
- [Snap confinement](https://snapcraft.io/docs/snap-confinement)
- [Snap commands and aliases](https://snapcraft.io/docs/commands-and-aliases)
- [The python snap plugin](https://snapcraft.io/docs/python-plugin)
- [Python command line scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
- [Snap interface management](https://snapcraft.io/docs/interface-management)
- [Build snaps from GitHub](https://snapcraft.io/docs/build-from-github)
- [Snapcraft hook support](https://snapcraft.io/docs/snapcraft-hook-support)
- [Adding snap configuration](https://snapcraft.io/docs/adding-snap-configuration)
- [Supported snap hooks](https://snapcraft.io/docs/supported-snap-hooks)
- [Snapcraft.yaml reference](https://snapcraft.io/docs/snapcraft-yaml-reference)
