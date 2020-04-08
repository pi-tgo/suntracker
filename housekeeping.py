#!/usr/bin/env python

import datetime, re
import shutil

# Make the filename to be the date - modify 
ARCHIVE_PATH = 'C:\\Temp\\archive\\'  # windows like path
#ARCHIVE_PATH = '/home/sun/archive/' # unix like path

yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
filename = ARCHIVE_PATH + yesterday.strftime('%Y-%m-%d.csv')

# Rutine to remove unwanted data in the file to be archived:
infile = open('latest.csv', 'r')
outfile = open(filename, 'a')

for line in infile:
    line = re.sub(line[:line.find("\"")], '', line)
    outfile.write(line)

infile.close()
outfile.close()

# Create a new latest.csv file
shutil.copy('header.csv', 'latest.csv')

