#Source: https://stackoverflow.com/questions/62397348/filenotfounderror-on-heroku-after-creating-that-file
class Logger:
    def __init__(self, name, file_handler, formatter, stream_handler):
        if not os.path.exists('Logs'):
            os.makedirs('Logs')

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        if stream_handler:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)


logger_dev = Logger('dev',
                    handlers.TimedRotatingFileHandler(f'Logs/dev.log', when='midnight', backupCount=2),
                    logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(message)s'),
                    True)

logger_usr = Logger('usr',
                    handlers.RotatingFileHandler(f'Logs/usr.log', maxBytes=7 * 1024 * 1024, backupCount=2),
                    logging.Formatter('%(asctime)s : %(message)s'),
                    False)