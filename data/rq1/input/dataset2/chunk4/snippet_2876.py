#Source: https://stackoverflow.com/questions/75594525/pytest-monkeypatching-dataclass-attribute-error
from dataclasses import dataclass
from pathlib import Path

@dataclass
class PathConfiguration:
    home: Path
    other: Path

@dataclass
class Configuration:
    path: PathConfiguration