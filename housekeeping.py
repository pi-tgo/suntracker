#!/usr/bin/python
#
# crontab: 4 0 * * * python housekeeping.py
# for å utføres kl. 0:04 hver natt

import datetime
import shutil

filename = str(datetime.date.today() + datetime.timedelta(days=-1)) + '.csv'

shutil.move('latest.csv', filename)
shutil.copy('header.csv', 'latest.csv')

