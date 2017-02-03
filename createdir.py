#!/usr/bin/python
import os, sys
os.chdir(os.getcwd());

# Path to be created
path = "/sound/player/footsteps/charger/run"

os.makedirs( path, 0755 );

print "Path is created"
