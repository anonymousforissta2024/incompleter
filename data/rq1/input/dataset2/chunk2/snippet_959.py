#Source: https://stackoverflow.com/questions/15737716/executor-map-typeerror-zip-argument-2-must-support-iteration
import time, concurrent.futures
lst100=[i for i in range(100)]

t1=time.clock()
print(list(map(str,lst100)))
t2=time.clock()
print(t2-t1)

t3=time.clock()
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = executor.map(str,lst100, 60)
    print(list(future_to_url))
t4=time.clock()
print(t4-t3)