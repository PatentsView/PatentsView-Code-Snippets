#Read-in script for Organization names and related agency hierarchy parsed from the government interest statements on all patents (where available)

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
dt = {'organization_id': 'int', 'name': 'str', 'level_one': 'str', 'level_two': 'str', 'level_three': 'str'}

file_name = "government_organization.tsv.zip"
f_name = "government_organization.tsv"
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
