#Source: https://stackoverflow.com/questions/68342294/what-is-the-cause-of-this-attribute-error
import utils
import remote_exec
import post
import get
import error_handler
import os
import handle_space
import socket
import json
from requests import get
import sys
import temp

def only_dest_requires_jumpserver():
    try:
        dictionary = {
            "migration_type": utils.config_data()["source_cloud"] + " to " + utils.config_data()["dest_cloud"]
        }

        utils.update_config_file(dictionary)
        print("\nInitialising " + utils.config_data()["source_cloud"] + " to " + utils.config_data()["dest_cloud"] + " migration...")
        hostname = socket.gethostname()

        if hostname == utils.config_data()["my_hostname"]:
            # get.call_get()
            temp.func()
            print("\nData successfully exported from source to this machine.\nChecking for space availability at jumpserver...")
            print("Done!")
    except Exception as error:
        filename = os.path.basename(__file__)
        error_handler.print_exception_message(error, filename)