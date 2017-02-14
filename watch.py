#!/usr/bin/env python

from os import listdir
import random
from subprocess import call
import ConfigParser


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

videodir= ConfigSectionMap("files")['videodir']
subdirs = ConfigSectionMap("files")['subdirs']
# path from where files should be fetched
#dirpath="/home/veli-v/Downloads/tuho"

videodir = videodir +'Family.Guy.S10'
print videodir
print subdirs
# Files to array
files=listdir( videodir )

# Debug print all files
for file in files:
    print file
print len(files)

# Randomize file
#filePlace = random.randint(0,6)
#print filePlace
#print files[filePlace]

# Watch the file
#command="mplayer"+videodir+"/"+files[filePlace]
#print command
#call(command, shell=True) 

# After watching move to watched folder so it does not come again.
#command="mv "+videodir+"/"+files[filePlace]+" "+dirpath+"/watched"
#print command
#call(command, shell=True) 
