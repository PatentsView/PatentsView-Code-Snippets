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
dt = {'uuid': 'str', 'patent_id': 'str', 'classification_level': 'str', 'section': 'str', 'ipc_class': 'str', 'subclass': 'str', 
        'main_group': 'str', 'subgroup': 'str', 'symbol_position': 'str', 'classification_value': 'str', 'classification_status': 'str', 
        'classification_data_source': 'str', 'action_date': 'str', 'ipc_version_indicator': 'str', 'sequence': 'int'}

# Selecting the zip file.
file_name = "ipcr.tsv.zip"
f_name = "ipcr.tsv"
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
