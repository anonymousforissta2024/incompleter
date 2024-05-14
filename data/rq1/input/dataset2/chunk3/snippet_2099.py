#Source: https://stackoverflow.com/questions/52298365/typeerror-when-writing-to-logfile
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='application.log', mode='a+')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)