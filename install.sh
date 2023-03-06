#! /bin/bash

VERSION=3.11
python${VERSION} -m venv venv-v${VERSION}
source venv-v${VERSION}/bin/activate
pip3 install --upgrade pip
pip3 install --requirement requirements-v${VERSION}.txt
