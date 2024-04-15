from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.values.str_to_float import StrToFloat
from main.actions.values.str_to_int import StrToInt
from main.actions.defines.define_keys import DefineKeys

import re
import ast
from enum import Enum

class _ValueError(ErrorBaseClass):
    mappings = {
        r'could not convert string to float: (\S+)': [ StrToFloat ],
        r'invalid literal for int\(\) with base 10: (\S+)': [ StrToInt ],
        r'not enough values to unpack \(expected (.* | )?(\d+), got (\d+)\)': [ DefineKeys ]
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        for err_msg_pattern, action_class_list in _ValueError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                kwargs = {}
                if err_msg_pattern in [ r'could not convert string to float: (\S+)', r'invalid literal for int\(\) with base 10: (\S+)' ]:
                    kwargs['class_name'] = m.groups()[0]
                elif err_msg_pattern in [ r'not enough values to unpack \(expected (.* | )?(\d+), got (\d+)\)' ]:
                    last_tbd = None
                    for iter_idx in range(self.snippet.current_iter-1, 0, -1):
                        if iter_idx in self.snippet.unpacked_tbds.keys():
                            last_tbd = self.snippet.unpacked_tbds[iter_idx]
                            break
                    if last_tbd is not None:
                        kwargs['class_name'] = last_tbd
                        kwargs['keys'] = list(range(int(m.groups()[1])))
                
                for ActionClass in action_class_list:
                    if (action := ActionClass(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                        return action
        
        return None