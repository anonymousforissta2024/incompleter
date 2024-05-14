#Source: https://stackoverflow.com/questions/75106915/error-pyflink-fn-execution-coder-impl-fast-intcoderimpl-encode-to-stream-typee
ds = stream_env.add_source(kafka_source, 'Kafka_Source')

ds = ds.map(transform_user_event_data,
            BaseEventSchema().get_type_info()).name('Transform_Data')

# ds.print()

stream_env.execute(cfg.JOB_NAME)   