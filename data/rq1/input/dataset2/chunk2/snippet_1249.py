#Source: https://stackoverflow.com/questions/68342294/what-is-the-cause-of-this-attribute-error
import requests
import json
import sys
import utils
import error_handler
import get_helper
import os
import pvdata

def call_get():
    try:
        auth_tuple = utils.get_auth_details("get")
        headers = utils.get_header()
        resource_types = utils.get_resource_types()
        namespaces = utils.get_namespaces()

        if resource_types[0].lower() == "all":
            resource_types = utils.append_all_resources()

        get_helper.get_namespace_list(auth_tuple, headers)
        all_namespaces = utils.extract_namespaces_from_list("source")

        if namespaces[0].lower() != "all":
            error_handler.validate_source_namespaces(namespaces, all_namespaces)

        utils.create_file(
            "Namespaces", "All_namespaces_at_source.txt", str(all_namespaces))

        get_helper.generate_json_for_all_namespaces(
            all_namespaces, auth_tuple, headers)

        for resource_name in resource_types:
            if namespaces[0].lower() == "all":
                for namespace in all_namespaces:
                    get_helper.call_all_functions_for_get(
                        namespace, resource_name, headers, auth_tuple)
            else:
                for namespace in namespaces:
                    get_helper.call_all_functions_for_get(
                        namespace, resource_name, headers, auth_tuple)
    except Exception as error:
        filename = os.path.basename(__file__)
        error_handler.print_exception_message(error, filename)

    return

if __name__ == "__main__":
    call_get()