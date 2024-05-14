#Source: https://stackoverflow.com/questions/73067007/typeerror-params-my-params-is-expected-to-be-class-params-myparams-but-val
import os
from dataclasses import dataclass
from pathlib import Path
import yaml
from decouple import config
from typed_json_dataclass import TypedJsonMixin


@dataclass
class MyParams(TypedJsonMixin):
    host: str
    project: str
    roi_term: str

    def __post_init__(self):
        self.public_key = config('KEY')
        assert isinstance(self.public_key, str)
        self.private_key = config('SECRET')
        assert isinstance(self.private_key, str)
        super().__post_init__()

# ...
@dataclass
class Params(TypedJsonMixin):
    my_params: MyParams
    # ...


def load_params_dict():
    parameter_file = 'params.yaml'
    cwd = Path(os.getcwd())
    params_path = cwd / parameter_file
    if params_path.exists():
        params = yaml.safe_load(open(params_path))
    else:  # If this script is being called from the path directory
        params_path = cwd.parent / parameter_file
        params = yaml.safe_load(open(params_path))
    return params


params_dict = load_params_dict()
print(params_dict)
project_params = Params.from_dict(params_dict)