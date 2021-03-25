#!/bin/bash

mkdir -p result
nix-build --out-link result/js js/build.nix
nix-build --out-link result/python python/build.nix
