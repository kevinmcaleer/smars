#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
git clone http://www.github.com/kevincaleer/smars 
pip install virtualenv
virtualenv venv
cd venv
pip install adafruit-pca9685
# sudo pipenv install
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
