#Source: https://stackoverflow.com/questions/58782469/python-class-inheritance-attributeerror-error-while-calling-child-class
import yaml
"""
Class created to read yaml files 
and extract requested literals seamlessly
"""

class GetConfig:
    @staticmethod
    def __check_values(*args):
        yaml = args[0]
        keys = args[1:]
        integrity = True
        arguments = [y for y, in yaml.items() if y not in keys]
        if len(arguments) > 0:
            integrity = False
        return integrity, arguments

    @classmethod
    def __load_yml(cls, yml_string):
        with open("{}.yml".format(yml_string), 'r') as stream:
                config = yaml.safe_load(stream)
        return config


class GetConnection(GetConfig):
    def __init__(self, server_name, username, db):
        """
        Generate database connection strings
            Arguments:
            :param server_name: as alphanumeric string
            :param username: as alphanumeric string
            :param db: as alphanumeric string
        """
        integrity, params = self.__check_values(self.__load_yml('connection_info'), server_name, username, db)
        if integrity is False:
            quit()
        self.server_name = server_name
        self.username = username
        self.db = db

    def __get_db_scope_access(self):
        config = self.__load_yml('connection_info')
        server = config['server'][self.server_name]['connection_string']
        user = config['server']['A']['databases'][self.db]['db_credentials'][self.username][0]
        passw = config['server']['A']['databases'][self.db]['db_credentials'][self.username][1]
        db = self.db
        return server, db, user, passw, config


if __name__ == "__main__":
    instance = GetConnection('A', 'claudio', 'mmd1')
    print(instance)
    str = instance.connection_string('mssql')
    print(str)