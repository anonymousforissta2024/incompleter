#Source: https://stackoverflow.com/questions/72963138/attributeerror-psutil-has-no-attribute-dirty
import psutil
mem = psutil.virtual_memory()
x.add_metric(schema.yy_MEMORY_DIRTY, mem.dirty)