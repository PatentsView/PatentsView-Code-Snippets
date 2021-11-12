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

# Specifies column types
dt = {'id': 'str', 'document number': 'str', 'type': 'str', 'application_number': 'str', 'date': 'str', 'country': 'str', 'series_code': 'int', 'invention_title': 'str', 'invention_abstract': 'str', 'rule_47_flag': 'str', 'filename': 'str'}

file_name = "application.tsv.zip"
f_name = "application.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
chunksize = 10 ** 4
count = 1
n_obs = 0
final = []
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC, dtype=dt):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
    final.append(df)
# Create data frame with all observations
df = pd.concat(final)
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)