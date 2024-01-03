VERSION := $(shell yq '.version' snap/snapcraft.yaml)

.PHONY: build
build:
	snapcraft --debug

.PHONY: install
install:
	sudo snap install pocketses_$(VERSION)_amd64.snap --dangerous
