#Source: https://stackoverflow.com/questions/47360506/typeerror-object-init-takes-no-parameters-trying-to-subclass-torch-floatt
import inspect
import torch

x = [[1, 2], [3, 4]]

print(torch.FloatTensor(x))
'''
 1  2
 3  4
[torch.FloatTensor of size 2x2]
'''

print(inspect.signature(torch.FloatTensor.__init__))
'''
(self, /, *args, **kwargs)
'''

class Image(torch.FloatTensor):
    def __init__(self, arg):
        print(inspect.signature(super().__init__))
        super().__init__(arg)

Image(x)
'''
(*args, **kwargs)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-369-4b1aee6414f6> in <module>()
     21         super().__init__(arg)
     22 
---> 23 Image(x)

<ipython-input-369-4b1aee6414f6> in __init__(self, arg)
     19     def __init__(self, arg):
     20         print(inspect.signature(super().__init__))
---> 21         super().__init__(arg)
     22 
     23 Image(x)

TypeError: object.__init__() takes no parameters
'''