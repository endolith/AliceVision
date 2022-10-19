#!/usr/bin/python
# This file is part of the AliceVision project.
# Copyright (c) 2016 AliceVision contributors.
# Copyright (c) 2012 openMVG contributors.
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse

# command line
parser = argparse.ArgumentParser(description='Sort sensor width camera database by the brand / model name')
parser.add_argument('-i', '--input', metavar='inputSensorDatabase.txt', required=True, type=str,
          help='File containing the original database of camera sensor widths')
parser.add_argument('-o', '--output', metavar='outputSensorDatabase.txt', required=True, type=str,
          help='File containing the sorted database of camera sensor widths')

args = parser.parse_args()

with open(args.input, "r") as file:
	database = file.readlines()
# process
sensors = [entry.split(';')  for entry in database]
sensors.sort(key=lambda t : tuple(s.lower() if isinstance(s,basestring) else s for s in t))
outDatabase = "".join(';'.join(entry) for entry in sensors)
with open(args.output, "w") as file:
	file.write(outDatabase)

