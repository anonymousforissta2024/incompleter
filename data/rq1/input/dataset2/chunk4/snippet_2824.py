#Source: https://stackoverflow.com/questions/60616722/typeerror-when-chunking-subtasks-in-grouped-tasks
#!/usr/bin/env python3

import argparse
from tasks import generate_file_from_output
import time

if __name__ == '__main__':
    # Arguments parsing :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--entries",
        help="set entries number",
        type=int,
        default=100,
        metavar="e",
    )
    # Multi process : one a worksheet?
    parser.add_argument("-m", "--multi", action="store_true")
    # Chunks : optimize by chunk (mutually exclusive with "multi_thread")
    parser.add_argument(
        "-c", "--chunks",
        help="perform the file generation by spliting the data to process into chunks",
        type=int,
        nargs="?",
        const=10,
        default=None,
        metavar="N",
    )
    parsed_args = parser.parse_args()
    print(parsed_args)
    result = generate_file_from_output(parsed_args)