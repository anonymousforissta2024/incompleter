#Source: https://stackoverflow.com/questions/75333088/class-typeerror-metawear-accelerometer-and-gyroscope
cb_fun = CFUNCTYPE(None, POINTER(Data))(data_handler)
libmetawear.mbl_mw_datasignal_subscribe(accelerometer, None, cb_fun)
libmetawear.mbl_mw_datasignal_subscribe(gyro, None, cb_fun)