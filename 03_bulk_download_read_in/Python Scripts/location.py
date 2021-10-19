#Read-in script for Disambiguated location data, including latitude and longitude

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np
pd.set_option('display.max_columns', None)
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt = {'id': 'str', 'city': 'str', 'state': 'str', 'country': 'str', 'latitude': 'float', 'longitude': 'float', 'county': 'str', 'state_fips': 'str', 'county_fips': 'str'}

file_name = "location.tsv.zip"
f_name = "location.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t", quoting=csv.QUOTE_NONNUMERIC, dtype=dt)
# Print first five observations
print(df.head())
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Provide additional information on certain variables.
print(df.describe(exclude=[np.number]))
