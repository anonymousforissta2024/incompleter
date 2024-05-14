#Source: https://stackoverflow.com/questions/75594525/pytest-monkeypatching-dataclass-attribute-error
import pytest
from my_module.settings import PathConfiguration, Configuration

@pytest.fixture
def configuration(monkeypatch, tmp_path):
    monkeypatch.setattr(Configuration.path, 'home', tmp_path)