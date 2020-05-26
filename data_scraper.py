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