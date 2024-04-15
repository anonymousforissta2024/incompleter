from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_key import DefineKey
from typing import Any
import ast

class DefineKeys(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.class_name = None
        if 'class_name' in kwargs.keys():
            self.class_name = kwargs['class_name']

        self.keys = None
        if 'keys' in kwargs.keys():
            self.keys = kwargs['keys']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Keys: {}\n'.format(self.keys)

        return desc

    def check_criteria(self) -> bool:
        if isinstance(self.keys, list):
            return True
        return False

    def apply_pattern(self) -> str:
        for key in self.keys:
            kwargs = {
                'class_name': self.class_name,
                'key': str(key)
            }
            if (define_key := DefineKey(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                define_key.apply_pattern()
        
        return

