#!/bin/bash

mkdir -p built
nix-build --out-link built/js js/build.nix
nix-build --out-link built/python python/build.nix
