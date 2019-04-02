#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
mkdir smars
cd smars
git clone https://github.com/kevinmcaleer/smars
sudo apt-get install virtualenv
virtualenv venv
# cd venv
source venv/bin/activate
pip install -r requirements.txt
# pip install adafruit-pca9685
# pip install smbus2
# sudo pipenv install
# sudo apt-get install python-smbus
sudo apt-get install i2c-tools
echo enabling i2c Interface
if grep -q 'i2c-dev' /etc/modules; then
  echo 'Seems i2c-dev module already exists, skip this step.'
else
  sudo echo 'i2c-dev' >> /etc/modules
fi
