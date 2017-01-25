#!/bin/bash

set -e -x

pushd newest/src
    pip install -r requirements.txt
    python tests.py
popd
