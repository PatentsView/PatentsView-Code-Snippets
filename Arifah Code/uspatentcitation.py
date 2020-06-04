#Read-in script for Citations made to US granted patents by US patents

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")
# Selecting the zip file.
file_name = "uspatentcitation.tsv.zip"
f_name = "uspatentcitation.tsv"
zf = zip.ZipFile(file_name)
chunksize = 2*(10 ** 6)
count = 1
n_obs = 0
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)



