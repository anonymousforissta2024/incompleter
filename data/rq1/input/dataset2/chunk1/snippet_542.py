#Source: https://stackoverflow.com/questions/28335048/struct-unpack-causing-typeerrorint-does-not-support-the-buffer-interface
length = struct.unpack('>B', data[34])[0]