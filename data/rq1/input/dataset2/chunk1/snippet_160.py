#Source: https://stackoverflow.com/questions/68088826/python-writing-avro-timestamp-millis-datum-astimezonetz-timezones-utc-attribu
writer = avro.io.DatumWriter(schema)
bytes_writer = io.BytesIO()
encoder = avro.io.BinaryEncoder(bytes_writer)
writer.write(get_dict(), encoder) #----------Exception here
raw_bytes = bytes_writer.getvalue()