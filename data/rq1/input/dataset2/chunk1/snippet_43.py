#Source: https://stackoverflow.com/questions/55401633/how-to-avoid-a-nameerror-when-making-an-alias-to-annotation-type-using-circular
from __future__ import annotations
import typing

MyType1 = typing.Union[str, MyType2]
MyType2 = typing.Mapping[str, MyType1]