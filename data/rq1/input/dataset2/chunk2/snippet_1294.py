#Source: https://stackoverflow.com/questions/27639305/typeerror-str-does-not-support-the-buffer-interface-configparser
# Load the configuration file
with open(CONFIG_FILE,'r+') as f:
    sample_config = f.read()
#config = ConfigParser.RawConfigParser(allow_no_value=True)
config = configparser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))        