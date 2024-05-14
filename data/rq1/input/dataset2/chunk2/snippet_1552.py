#Source: https://stackoverflow.com/questions/72690805/python-inheriting-generic-type-typeerror-object-init-takes-exactly-one-a
# sprite.py
from typing import TypeVar, Generic

T = TypeVar('T', bound=Object)

class Sprite(Generic[T]):
  def __init__(self, **kwargs):
    super(Sprite, self).__init__(self, clickable=True, evt_handler=self.click_wrapper, **kwargs)