#Read-in script for Persistant Assignee Disambiguation

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt = {'rawassignee_id': 'str', 'disamb_assignee_id_xxxxxxxx': 'str'}

# Selecting the zip file.
file_name = "persistent_assignee_disambig.tsv.zip"
f_name = "persistent_assignee_disambig.tsv"
zf = zip.ZipFile(file_name)
chunksize = 10 ** 6
count = 1
n_obs = 0
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC, dtype=dt):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of columns, observations, and each variable data type
print(n_obs)
print(df.dtypes)
