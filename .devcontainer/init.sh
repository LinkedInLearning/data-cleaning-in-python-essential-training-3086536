#!/bin/bash

set -e
set -x

python -m pip install --upgrade pip
python -m pip install -r ${localWorkspaceFolder}/requirements.txt
echo "PS1='$ '" >> ~/.bashrc
