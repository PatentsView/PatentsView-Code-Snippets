#Read-in script for International Patent Classification data for all patents (as of publication date)

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
pd.set_option('display.max_columns', None)
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# Specifies column types
dt ={'id': 'str', 'document_number': 'str', 'sequence': 'int', 'version': 'str', 'class_level': 'str', 'section': 'str', 'class': 'str', 'subclass': 'str', 'main_group': 'str', 'subgroup': 'str', 'symbol_position': 'str', 'class_value': 'str', 'action_date': 'str', 'class_status': 'str', 'class_data_source': 'str'}

# Selecting the zip file.
file_name = "ipcr.tsv.zip"
f_name = "ipcr.tsv"
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