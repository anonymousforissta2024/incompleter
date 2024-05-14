#Source: https://stackoverflow.com/questions/67015675/getting-unsupported-operand-type-error-while-trying-to-subtract-two-date-values
from datetime import datetime
import time
start =datetime.now().replace(microsecond=0).isoformat(' ')
end = datetime.now().replace(microsecond=0).isoformat(' ')
print(f" Total Time taken by check run is {end - start}[hh:mm:ss]")