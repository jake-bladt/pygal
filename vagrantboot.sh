#!/usr/bin/env bash

apt-get update

# install python
apt-get install python-dev python-pip git -q -y

export GALLERY_ROOT=/assets/subjects
