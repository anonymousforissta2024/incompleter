#Source: https://stackoverflow.com/questions/58179496/logging-error-in-python-3-x-typeerror-a-bytes-like-object-is-required-not-s
if __name__ == '__main__':
    config_file = '/source/account_content_recommendation/config/sales_central_config.json'
    try:
        ### Read all the parameters -
        params = json.loads(hdfs.read_file(config_file))

        ### Create the logging csv file -
        hdfs_log_path = params["hdfs_log_path"]
        hdfs.create_file(hdfs_log_path, "starting ... ", overwrite = True)
        log_name = 'Account_Content_Matching'


        global stream
        log = logging.getLogger('Acct_Cont_Log')
        stream = BytesIO()
        handler = logging.StreamHandler(stream)
        log.setLevel(logging.DEBUG)

        for handle in log.handlers:
            log.removeHandler(handle)

        log.addHandler(handler)

        #env = sys.argv[1]
        env = 'dev'
        formatter = logging.Formatter('{0}| %(asctime)s| {1}| %(module)s| %(funcName)s| %(lineno)d| %(levelname)s| %(message)r'.format(log_name, env))
        handler.setFormatter(formatter)

        log.info("starting execution of Account_Content_Matching load")
        #log.info("sys args %s"%(str(sys.argv)))

        def flush_log():
            global stream
            msg = stream.getvalue()
            hdfs.append_file(hdfs_log_path, msg)
            stream.seek(0)
            stream.truncate(0)
            print(msg)
            sys.stdout.flush

    except Exception as error:
        raise error