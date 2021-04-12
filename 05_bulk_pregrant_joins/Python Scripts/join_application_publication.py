# Read-in script for joining the pre-granted application and publication tables
# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

# specify the name of the application zip file and the name you want to use when unzipped
app_zip = "application.tsv.zip"
app = "application.tsv"

# specify the name of the publication zip file and the name you want to use when unzipped
pub_zip = "publication.tsv.zip"
pub = "publication.tsv"

# Selecting the zip files
zf_app = zip.ZipFile(app_zip)
zf_pub = zip.ZipFile(pub_zip)

# Read the data into dataframes
df_app = pd.read_csv(zf_app.open(app), delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)
df_pub = pd.read_csv(zf_pub.open(pub), delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)

# Rename columns which are the same across both files
df_app = df_app.rename(columns={'id':'id_app', 'date':'date_app', 'country':'country_app'})
df_pub = df_pub.rename(columns={'id':'id_pub', 'date':'date_pub', 'country':'country_pub'})

# Merge the two dataframes together
merged = df_pub.merge(df_app, how="inner", on='document_number')

# print the first 5 columns and the length of the dataframe
print(merged.head())
print(len(merged))