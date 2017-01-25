#!/bin/bash

set -e -x

pushd newest/src/newest
    pip install -r requirements.txt
    python tests.py
popd
