#!/bin/bash

mkdir -p built_images
nix-build --out-link result/js js/build.nix
nix-build --out-link result/python python/build.nix
