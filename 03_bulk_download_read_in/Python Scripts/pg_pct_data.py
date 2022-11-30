#Read-in script for PCT data

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
file_name = "pg_pct_data.tsv.zip"
f_name = "pg_pct_data.tsv"
# Selecting the zip file.
with zip.ZipFile(file_name) as zf:
# Reading the selected file in the zip.
    with zf.open(f_name) as openfile: 
        df = pd.read_csv(openfile, delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)
# Print first five observations
print(df.head())
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Provide additional information on certain variables.
print(df.describe(exclude=[np.number]))