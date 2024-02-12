#!/usr/bin/env python3
"""
========
Overview
========


=====
Usage
=====

    
==========
ChangeLog
==========
V0.1 20230201 Yagizalp OKUR
"""
import argparse
import math

def convert2int(south,north,west,east):
    n_south=math.floor(south)
    n_north=math.ceil(north)
    n_west=math.floor(west)
    n_east=math.ceil(east)
    output=str(n_south)+","+str(n_north)+","+str(n_west)+","+str(n_east)
    print(output)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert to integers",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("south", type=float, help="South limit")
    parser.add_argument("north", type=float, help="North limit")
    parser.add_argument("west", type=float, help="West limit")
    parser.add_argument("east", type=float, help="East limit")


    args = parser.parse_args()

    convert2int(args.south, args.north, args.west, args.east)
