#Source: https://stackoverflow.com/questions/40500717/typeerror-cant-pickle-generator-objects-for-non-generator-methods
import inspect
print(inspect.isgeneratorfunction(self.checkProcess))