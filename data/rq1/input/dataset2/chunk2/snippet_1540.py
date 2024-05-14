#Source: https://stackoverflow.com/questions/67095534/forwardreference-nameerror-when-loading-a-recursive-dict-in-dataclass
import marshmallow_dataclass
from dataclasses import field
from api_handler import BaseSchema
from typing import Sequence, Union, Literal, Type, List, ForwardRef, TypeVar, Generic

filter_input = { "rules" :
  [{
    "groupOperator" : "and",
    "expressions" : [
      { "field": "xxxxx", "operator": "eq", "value": 'level1' },
      { "field": "xxxxx", "operator": "eq", "value": 'm'},
      { "field": "xxxxx", "operator": "eq", "value": "test"},
      {
        "groupOperator" : "or",
        "expressions" : [
          { "field": "xxxx", "operator": "eq", "value": 'level2' },
          { "field": "xxxx", "operator": "eq", "value": 'm' },
          { "field": "xxxx", "operator": "eq", "value": "test" }
        ]
      }
    ]
  }]
}