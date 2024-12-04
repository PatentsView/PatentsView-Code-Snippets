import yaml
import subprocess
import pytest
from testbook import testbook

# Change the working directory to the Data Downloads folder for all tests in this file.
@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch):
    monkeypatch.chdir('Data Downloads')


@testbook('Data Downloads/0-introduction.ipynb', execute=True)
def test_0_introduction(nb):
    ...  # Just check that notebook runs without error.


def test_sources():
    with open("sources.yml") as file:
        sources = yaml.safe_load(file)
    
    for data in [sources['granted'], sources['pre-grant']]:
        for source in data.values():
            database = source['database']
            url_template = source['url_template']
            for table in source['tables']:
                table_url = url_template.format(database=database, table=table)
                
                print("Checking ", table_url)
                subprocess.run(['curl', '--head', '--fail', table_url], check=True)