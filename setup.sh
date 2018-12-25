#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
git clone https://github.com/kevinmcaleer/smars.git
sudo pip install virtualenv
cd smars
virtualenv venv
# cd venv
source venv/bin/activate
pip install adafruit-pca9685
pip install smbus2
# sudo pipenv install
# sudo apt-get install python-smbus
sudo apt-get install i2c-tools
echo enabling i2c Interface
if grep -q 'i2c-dev' /etc/modules; then
  echo 'Seems i2c-dev module already exists, skip this step.'
else
  sudo echo 'i2c-dev' >> /etc/modules
fi
