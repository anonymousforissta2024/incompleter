#Source: https://stackoverflow.com/questions/67095534/forwardreference-nameerror-when-loading-a-recursive-dict-in-dataclass
@marshmallow_dataclass.dataclass(base_schema=BaseSchema)
class Expression:
    field    : str
    operator : str
    value    : str 

@marshmallow_dataclass.dataclass(base_schema=BaseSchema)
class LogicalGroup:
    group_operator   : str
    expressions      : List[Union['LogicalGroup', Expression]] = field(default_factory=list)
  
@marshmallow_dataclass.dataclass(base_schema=BaseSchema)
class Filter:
    rules: List[LogicalGroup] = field(default_factory=list)