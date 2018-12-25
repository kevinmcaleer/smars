#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
echo
sudo pip install pipenv
sudo pipenv install
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
