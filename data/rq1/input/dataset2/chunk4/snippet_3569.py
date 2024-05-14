#Source: https://stackoverflow.com/questions/75333088/class-typeerror-metawear-accelerometer-and-gyroscope
import time
from mbientlab.metawear import MetaWear, libmetawear
from mbientlab.metawear.cbindings import *
from mbientlab.warble import *
from mbientlab.metawear import *
from threading import Event
from time import sleep
import ctypes

# Define the data handler method
def data_handler(data):
    print("Accelerometer data: x = {0:.3f}, y = {1:.3f}, z = {2:.3f}".format(data['accelerometer'][0], data['accelerometer'][1], data['accelerometer'][2]))
    print("Gyro data: x = {0:.3f}, y = {1:.3f}, z = {2:.3f}".format(data['gyro'][0], data['gyro'][1], data['gyro'][2]))

# Create a state object to store information about the device and the number of data samples received
class State:
    def __init__(self, device):
        self.device = device
        self.samples = 0

# Connect to the device using its MAC address
device = MetaWear("ADDRESS")
device.connect()

# Set the connection parameters
libmetawear.mbl_mw_settings_set_connection_parameters(device.board, 7.5, 7.5, 0, 6000)

# Configure the accelerometer
libmetawear.mbl_mw_acc_set_odr(device.board, 100)
libmetawear.mbl_mw_acc_set_range(device.board, 8.0)
libmetawear.mbl_mw_acc_write_acceleration_config(device.board)

# Configure the gyro
libmetawear.mbl_mw_gyro_bmi160_set_odr(device.board, 100)
libmetawear.mbl_mw_gyro_bmi160_set_range(device.board, 2000)
libmetawear.mbl_mw_gyro_bmi160_write_config(device.board)

# Create a state object and subscribe to the accelerometer and gyro data streams
state = State(device)
accelerometer = libmetawear.mbl_mw_acc_get_acceleration_data_signal(device.board)
gyro = libmetawear.mbl_mw_gyro_bmi160_get_rotation_data_signal(device.board)

cb_fun = CFUNCTYPE(None, POINTER(Data))(data_handler) # NOT WORKING
libmetawear.mbl_mw_datasignal_subscribe(accelerometer, None, cb_fun) # NOT WORKING
libmetawear.mbl_mw_datasignal_subscribe(gyro, None, cb_fun) # NOT WORKING

# Start streaming dat
libmetawear.mbl_mw_acc_enable_acceleration_sampling(device.board)
libmetawear.mbl_mw_gyro_bmi160_enable_rotation_sampling(device.board)
libmetawear.mbl_mw_acc_start(device.board)
libmetawear.mbl_mw_gyro_bmi160_start(device.board)

#Wait for 5 seconds
time.sleep(5.0)

#Stop the accelerometer and gyro
libmetawear.mbl_mw_acc_stop(device.board)
libmetawear.mbl_mw_gyro_bmi160_stop(device.board)

#Disable acceleration and rotation sampling
libmetawear.mbl_mw_acc_disable_acceleration_sampling(device.board)
libmetawear.mbl_mw_gyro_bmi160_disable_rotation_sampling(device.board)

#Disconnect from the device
device.disconnect()