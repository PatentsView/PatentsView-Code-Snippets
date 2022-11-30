#Read-in script for Number of figures and sheets

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

file_name = "g_attorney_not_disambiguated.tsv.zip"
f_name = "g_attorney_not_disambiguated.tsv"
# Selecting the zip file.
with zip.ZipFile(file_name) as zf:
# Reading the selected file in the zip.
    with zf.open(f_name) as openfile: 
        df = pd.read_csv(openfile, delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)

# Print first five observations
df.head()
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Print basic summary statistics for numerical variables
print(df.describe(exclude=[np.number]))