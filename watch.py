#!/usr/bin/env python

from os import listdir
import random
from subprocess import call

dirpath="/home/veli-v/Downloads/tuho"
files=listdir( dirpath )
for file in files:
	print file
print len(files)

filePlace = random.randint(0,6)
print filePlace
print files[filePlace]

command="mplayer "+dirpath+"/"+files[filePlace]
print command
call(command, shell=True) 
command="mv "+dirpath+"/"+files[filePlace]+" "+dirpath+"/watched"
print command

call(command, shell=True) 
