import yaml
import subprocess
import pytest
from testbook import testbook


# Change the working directory to the Data Downloads folder for all tests in this file.
@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch):
    monkeypatch.chdir("data-downloads")


@testbook("data-downloads/0-getting-started.ipynb", execute=True)
def test_0_introduction(nb):
    """Check that notebook runs without error."""
    ...


def test_sources():
    """Check that all urls in sources.yml are valid."""
    with open("sources.yml") as file:
        sources = yaml.safe_load(file)

    for data in [sources["granted"], sources["pre-grant"]]:
        for source in data.values():
            # E.g. database = 'https://s3.amazonaws.com/data.patentsview.org/download'
            database = source["database"]
            url_template = source["url_template"]
            for table in source["tables"]:
                # E.g. table_url = https://s3.amazonaws.com/data.patentsview.org/download/g_patent.tsv.zip
                table_url = url_template.format(database=database, table=table)

                print("Checking ", table_url)
                subprocess.run(["curl", "--head", "--fail", table_url], check=True)
