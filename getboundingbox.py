#!/usr/bin/env python3
"""
========
Overview
========
This scripts calculates the smallest bounding box using the information from
alos2Proc.xml ISCE baseline step.

=====
Usage
=====
Execute the script in the main folder. The main folder needs to have process
folders in yyyymmdd_yyyymmdd format.
    
==========
ChangeLog
==========
V0.1 20230119 Yagizalp OKUR
"""
import glob
import os
import re

directory=os.getcwd()+"/????????_????????"
entries=(glob.glob(directory))
lims=[]
for entry in entries:
    f=open(entry+"/alos2Proc.xml")
    for line in f:
        if re.search("reference_bounding_box", line):
            lims.append(line)
        if re.search("secondary_bounding_box", line):
            lims.append(line)
newlims=[]            
for line in lims:
    newlims.append(line[33:109])
south=[]
north=[]
west=[]
east=[]
for line in newlims:
    temp=line.split(", ")
    south.append(float(temp[0]))
    north.append(float(temp[1]))
    west.append(float(temp[2]))
    east.append(float(temp[3]))

bounding_box=str(round(max(south),6))+","+str(round(min(north),6))+","+str(round(max(west),6))+","+str(round(min(east),6))
print(bounding_box)

    
