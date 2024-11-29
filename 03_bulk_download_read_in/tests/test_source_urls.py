import yaml
import subprocess

with open("03_bulk_download_read_in/Python Scripts/sources.yml") as file:
    sources = yaml.safe_load(file)

for source in sources.values():
    database_url = source['database']
    for table_name in source['tables']:
        table_url = f"{database_url}/{table_name}.tsv.zip"
        
        print("Checking ", table_url)
        subprocess.run(['curl', '--head', '--fail', table_url], check=True)
        