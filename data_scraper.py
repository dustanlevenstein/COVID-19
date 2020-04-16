#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:08:26 2020

@author: dustan
"""

import os
import pandas as pd
for directory, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename[-3:] == 'csv':
            print("Found a csv!")