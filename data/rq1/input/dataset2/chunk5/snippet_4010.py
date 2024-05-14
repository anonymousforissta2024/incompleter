#Source: https://stackoverflow.com/questions/38032782/why-is-my-logstash-handler-throwing-a-typeerror
import logging
import logstash

from socket import gethostname

class CustomLogger(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None):
        if extra is None:
            extra = { 'hostname' : gethostname() }
        super(CustomLogger, self)._log(level, msg, args, exc_info, extra)

def setup_custom_logger(host, port):
    # add hostname to the formatter.
    logging.setLoggerClass(CustomLogger)

    formatter = logging.Formatter(fmt='%(hostname)s - %(asctime)s - %(levelname)s - %(module)s - %(message)s')

    logstash_handler = logstash.LogstashHandler(host, port, version=2)
    logstash_handler.setLevel(logging.DEBUG)
    logstash_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logstash_handler)

    return logger