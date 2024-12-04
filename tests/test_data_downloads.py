import pytest
from testbook import testbook

@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch):
    monkeypatch.chdir('Data Downloads')


@testbook('Data Downloads/0-introduction.ipynb', execute=True)
def test_0_introduction(nb):
    ...  # Just check that notebook runs without error.
