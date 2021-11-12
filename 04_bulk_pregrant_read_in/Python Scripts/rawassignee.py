#Read-in script for Raw inventor information as it appears in the source text and XML files
# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt ={'id': 'str', 'document_number': 'str', 'assignee_id': 'str', 'sequence': 'int', 'name_first': 'str', 'name_last': 'str', 'organization': 'str', 'type': 'int', 'rawlocation_id': 'str', 'city': 'str', 'state': 'str', 'country': 'str'}

# Selecting the zip file.
file_name = "rawinventor.tsv.zip"
f_name = "rawinventor.tsv"
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