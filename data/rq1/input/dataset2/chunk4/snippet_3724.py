#Source: https://stackoverflow.com/questions/60919083/getting-unexpected-nonetype-error-in-python
import worker

def multiply_worker_value(arguments):
    current_Worker = arguments[0]
    multiplier = arguments[1]
    new_worker = current_Worker.change_value(multiplier)
    return new_worker

current_worker = worker.Worker()
print("Printing value:")
print(current_worker.get_value()[0])

while(current_worker.get_value()[0] < 10):
    paramList = [current_worker,2]
    current_worker = multiply_worker_value(paramList)
print(current_worker.get_value()[0])