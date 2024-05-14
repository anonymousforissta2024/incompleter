#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
#-*- coding: utf-8 -*-
import sha3
import pyopencl as cl
import Keccak
import time
#Initialize OpenCL
platforms = cl.get_platforms()
devices = platforms[0].get_devices()
context = cl.Context(devices[:2])
queue = cl.CommandQueue(context, context.devices[0],
                        properties=cl.command_queue_properties.PROFILING_ENABLE)
program = cl.Program(context, open('sha3.cl').read()).build(options='')

#Parameters for SHA 512
r = 576
c = 1024
n = 512

inputlist = []
inputlist.append("a" * 1000)


start = time.time()
result = sha3.Keccak(inputlist, n, r,c, program, context, queue)
print  ("Hashing Result is")
print (result)
print ("Time taken is: " + str(time.time() - start))