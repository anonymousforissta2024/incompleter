#Source: https://stackoverflow.com/questions/60541782/attributeerror-when-patching-class-variable-when-mocking
from mocking_module.sample_class import SampleClass

def do_something():
    sample_class = SampleClass()
    return sample_class.get_base_url()