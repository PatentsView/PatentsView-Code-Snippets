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
dt = {'uuid': 'str', 'patent_id': 'str', 'rawlocation_id': 'str', 'name_first': 'str', 'name_last': 'str', 'organization': 'str', 'sequence': 'int', 'designation': 'str', 'applicant_type': 'str'}

file_name = "non_inventor_applicant.tsv.zip"
f_name = "non_inventor_applicant.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC, dtype=dt)

# Print first five observations
df.head()
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Print basic summary statistics for numerical variables
print(df.describe(exclude=[np.number]))