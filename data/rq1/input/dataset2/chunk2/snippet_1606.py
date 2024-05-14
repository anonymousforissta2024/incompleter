#Source: https://stackoverflow.com/questions/75174299/pyflink-sliding-window-on-a-datastream-fails-with-attributeerror
input_stream = self.table_env.to_data_stream(flat_table)
result_stream = input_stream.key_by(get_key) \
    .window(CountSlidingWindowAssigner.of(self.window_size, self.window_slide)) \
    .apply(MyWindowFunction(),
           output_type=Types.TUPLE([Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.FLOAT(), Types.FLOAT(), Types.FLOAT()]))