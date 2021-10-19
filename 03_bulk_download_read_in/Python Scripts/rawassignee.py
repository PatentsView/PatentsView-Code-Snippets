#Read-in script for Raw assignee information as it appears in the source text and XML files

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt = {'uuid': 'str', 'patent_id': 'str', 'assignee_id': 'str', 'rawlocation_id': 'str', 'type': 'int', 'name_first': 'str', 'name_last': 'str', 'organization': 'str', 'sequence': 'int'}

# Selecting the zip file.
file_name = "rawassignee.tsv.zip"
f_name = "rawassignee.tsv"
zf = zip.ZipFile(file_name)
chunksize = 10 ** 6
count = 1
n_obs = 0
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC, dtype=dt):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)
