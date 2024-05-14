from array import array
import binascii
print('array1:', array1)
as_bytes = array1.tobytes()
print('Bytes:', binascii.hexlify(as_bytes))
array2 = array('i')
array2.frombytes(as_bytes)
print('array2:', array2)