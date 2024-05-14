#Source: https://stackoverflow.com/questions/25054729/delattr-on-class-instance-produces-unexpected-attributeerror
class __Sysconfig(Config):
    """
    H.O.M.I.E.'s system configuration
    """
    ### Application information ###
    APP_NAME = 'H.O.M.I.E.'
    APP_VER = '0.1-indev'
    APP_FULL_NAME = "Cool system"

    ### System logging ###
    LOG_DIR = '/var/log/homie.d'
    LOGFILE = '/var/log/homie'
    LOGLVL = 2

    ### System files ###
    DAEMON_SERVICES_FILE = '/var/run/homie.services'
    DAEMON_SOCK = 'tcp://127.0.0.1'
    GLOBAL_CONFIG_DIR = '/usr/local/etc/homie.d'

    ### System EMail ###
    EMAIL_FROM = 'homie@company.com'
    TECH_EMAIL = 'me@company.com'
    ADMIN_EMAILS = ['me@company.com', 'other@company.com']

    def __init__(self):
        """
        Creates a sysconfig instance
        """
        super().__init__('/usr/local/etc/homie')