#Source: https://stackoverflow.com/questions/50716931/unittest-mock-and-multiple-inheritance-typeerror-metaclass-conflict
import sys
from unittest import mock

# inspired by https://stackoverflow.com/a/37363830/1860757
MOCK_MODULES = ['class_a', ]
sys.modules.update((mod_name, mock.MagicMock()) for mod_name in MOCK_MODULES)

import code

code.C()