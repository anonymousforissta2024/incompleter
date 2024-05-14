#Source: https://stackoverflow.com/questions/37163806/python-multiprocessing-attributeerror-str-object-has-no-attribute-has
import multiprocessing
p = multiprocessing.Pool(max_processes)
p.map(worker_function, input_data) # trigger the error