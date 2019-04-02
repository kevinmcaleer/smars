# SMARS
Screwless Modular Assemblable Robotic System

![Build Status](https://travis-ci.com/kevinmcaleer/smars.svg)

## SMARSfan.com
Visit www.smarsfan.com for more information about this project. The site includes build instructions, videos, an interview with the designer and much more.

## About this library
This library will enable you to get the quad robot walking and detecting its environment.

## Python Library now pulls from pip
There is now a SMARS Python library available via pip.

***Make sure you follow the instructions below to ensure the virtual environment is setup correctly and everything should work perfectly.***

## Setup a virtual environment
The best way to ensure all the right prerequisites are installed and the supported version of python is installed is by setting up a virtual environment for python.

To Install virtualenv:
* log on to your raspberry pi
* install virtualenv:
`sudo apt-get install virtualenv`
* create a new virtual python environment:
`virtualenv -p python3 venv`
* activate the new python environment:
`source venv/bin/activate`
* install the pre-requisites:
`pip install -r requirements.txt`
* to deactivate the environment once you have finished, type `deactivate`

## Scratch 1.4 Code  
The Library now includes a sample Scratch 1.4 script that will enable you to control your SMARS Quad robot from the scratch environment. Please note you will need to enable the remote sensor control for this to work, by right clicking on the sensor and clicking on 'enable remote sensing'.

The Scratch demo script needs to communicate with the Python 'ScratchListener.py' code, and you will need to know the IP address of the computer running Scratch 1.4.

Note only Scratch 1.4 has the 'enable remote sensing' option available, Scratch 2.0 & Scratch 3.0 do not allow this, however you can still download and use Scratch 1.4 from the Scratch website: http://scratch.mit.edu

Link to thingiverse original model:
https://www.thingiverse.com/thing:2662828

Link to Quad version
https://www.thingiverse.com/thing:2755973

# Overview and Background
## SMARS

This robot is really easy and cheap to 3d print, build and program. It can be assembled without screws or soldering and it's modular so it can be adapted for different purposes. I'm Swiss, so I don't know American scholastic system but I would use SMARS in last year of middle school, high school or universities/ colleges. There is more "open electronics" compared to a Lego NXT or similar, so students need a few knowledges about security, electrical laws and so on. It can be use to improve software development skills, CAD skills or electronics skills, students can design their own modules and customize their SMARS.

## Programming SMARS
You can use most common small hardware platforms as the brains inside SMARS, the Arduino platform (and compatible) was used in the original design as its cheap, commonly available, and the tools for programming it are easy to use. For the quad version of the robot a Raspberry Pi Zero was used. The language commonly used on the Pi (and where it gets it name from) is Python. A library module has been written for both Arduino and Python to help you get started.

## Getting the Arduino IDE
Visit http://www.arduino.cc to download the latest Arduino Integrated Development Environment (IDE).
