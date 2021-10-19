#Read-in script for Current USPC classification data for all patents up to May 2015

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt = {'uuid': 'str', 'patent_id': 'str', 'mainclass_id': 'str', 'subclass_id': 'str', 'sequence': 'int'}

# Selecting the zip file.
file_name = "uspc_current.tsv.zip"
f_name = "uspc_current.tsv"
zf = zip.ZipFile(file_name)
chunksize = 15*(10 ** 5)
count = 1
n_obs = 0
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC, dtype=dt):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)
