#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:45:51 2024

@author: benhenderson
"""

import pandas as pd

data_file = pd.read_csv("for_nitpicker.dat", delimiter = "\t", header = None)
column_names = ["Date", "Time", "Depth (m)", "Temperature", "Salinity (psu)"]
data_file.columns = column_names
print(data_file.head())

data_file.to_csv("20081129-CTD_data.dat", sep = "\t", header = True, index = False)

