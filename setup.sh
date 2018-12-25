#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
git clone https://github.com/kevinmcaleer/smars.git
pip install virtualenv
cd smars 
virtualenv venv
cd venv
pip install adafruit-pca9685
# sudo pipenv install
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
