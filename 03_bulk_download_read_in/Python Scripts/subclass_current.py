#Read-in script for Number of figures and sheets

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("//dc1fs/dc1ehd/share/Science Policy Portfolio/PatentsView IV/Documentation/Tables/20200331")

file_name = "subclass_current.tsv.zip"
f_name = "subclass_current.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t")

# Print first five observations
df.head()
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()
# Print basic summary statistics for numerical variables
print(df.describe(df.select_dtypes(include='int')))