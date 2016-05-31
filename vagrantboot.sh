#!/usr/bin/env bash

apt-get update

# install python
apt-get install python-dev python-pip -q -y

export GALLERY_ROOT=/assets/subjects
