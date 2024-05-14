#Source: https://stackoverflow.com/questions/69212086/attributeerror-in-pydantic-while-assigning-value-in-class
from pydantic import BaseModel

class somefirst(BaseModel):
      flag: bool = False