#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:08:26 2020

@author: dustan
"""

import os
import pandas as pd
dataframes = {}
for directory, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename[-3:] == 'csv':
            fullpath = os.path.join(directory, filename)
            dataframes[fullpath] = pd.read_csv(fullpath)

keys = list(dataframes.keys())
keys.sort()

# Select the dataframes which occur in the 'csse_covid_19_daily_reports'
# subdirectory.
standardized_keys = [pathname for pathname in keys 
                     if os.path.split(os.path.split(pathname)[0])[-1]
                         == 'csse_covid_19_daily_reports']

def extract_ymd(filepath):
    return tuple(map(int, os.path.split(filepath)[-1].split('.')[0].split('-'))
                 )

dated_data_frames = {extract_ymd(filepath) : dataframes[filepath]
                     for filepath in standardized_keys}
columns = {}
previous_columns = None
for key in sorted(dated_data_frames.keys()):
    if tuple(dated_data_frames[key].columns) != previous_columns:
        previous_columns = tuple(dated_data_frames[key].columns)
        columns[key] = previous_columns
        
# columns
# Out[26]: 
# {(1, 22, 2020): ('Province/State',
#   'Country/Region',
#   'Last Update',
#   'Confirmed',
#   'Deaths',
#   'Recovered'),
#  (3, 1, 2020): ('Province/State',
#   'Country/Region',
#   'Last Update',
#   'Confirmed',
#   'Deaths',
#   'Recovered',
#   'Latitude',
#   'Longitude'),
#  (3, 22, 2020): ('FIPS',
#   'Admin2',
#   'Province_State',
#   'Country_Region',
#   'Last_Update',
#   'Lat',
#   'Long_',
#   'Confirmed',
#   'Deaths',
#   'Recovered',
#   'Active',
#   'Combined_Key')}