#Source: https://stackoverflow.com/questions/64679139/nameerror-name-open-is-not-defined-when-trying-to-log-to-files
handler = logging.FileHandler(
    filename="../logs/bot.log",
    mode="a")
formatter = logging.Formatter("%(asctime)s %(name)-30s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(handler)