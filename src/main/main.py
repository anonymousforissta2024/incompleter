from path_config import PROJECT_DIR, DATA_DIR, LOG_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor
from main.utils.snippet import Snippet
from main.utils.session import Session

import os
import sys
import json
import argparse
import traceback
from glob import glob
from tqdm import tqdm

aggregate_deductions = defaultdict(int)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', metavar='target_directory', help='The directory where the target snippets are located. The path should be with relative to the DATA_DIR of the project. Please check "src/path_config.py" for DATA_DIR reference. Possible value for this argument is most likely one of the following: ["lexecutor_success", "lexecutor_fail"]')
    parser.add_argument('-s', '--snippet_name', dest='snippet_name', metavar='snippet_name (optional)', help='If you wish to run for a single snippet, please specify the name of the snippet through this argument. E.g. "snippet_47.py.orig"', default='.py.orig')
    parser.add_argument('-c', '--cov', action='store_true', dest='cov', help='If you wish to compute code coverage while moxecuting the code, you can use this argument to specify that. Possible values are either True or False. Defaults to False.')
    parser.add_argument('-cdata', '--cdata', action='store_true', dest='cdata', help='If you wish to create a dataset with/without mock augmentation, set this flag. When setting this flag, ensure that the type dictionary (assignments_info.json) exists in the correct path. Possible values are either True or False. Defaults to False.')
    parser.add_argument('-lextp', '--lextp', action='store_true', dest='lextp', help='Use this flag to enable  LexTP for prediction. Possible values are either True or False. Defaults to False.')
    parser.add_argument('-inctp', '--inctp', action='store_true', dest='inctp', help='Use this flag to enable IncTP for prediction. Possible values are either True or False. Defaults to False.')
    args = parser.parse_args()

    path=os.path.join(DATA_DIR, args.dir)
    Session.lextp = args.lextp or args.inctp
    Session.inctp = args.inctp

    # Only when creating IncompleterNN's dataset, open the assignments_info.json to retrieve the type information of the undefined variables from the ground_truth_dataset
    type_dict_path, type_dicts = None, None
    if args.cdata:
        type_dict_path = os.path.join(DATA_DIR, "new_all/dataset3/assignments_info.json")
        if os.path.exists(type_dict_path):
            with open(type_dict_path, 'r') as type_dict_file:
                type_dicts = json.load(type_dict_file)

    print()
    for file_name in tqdm(glob(os.path.join(path, '*'+args.snippet_name)), desc='Moxecution (mock+execution) Progress'):
        file_path = os.path.join(path, file_name)
        
        try:
            mox = Moxecutor(snippet_path=file_path, is_cov=args.cov, type_dict=type_dicts[file_name.split('/')[-1].replace('snippet_', '').replace('.py.orig', '')]) if args.cdata else Moxecutor(snippet_path=file_path, is_cov=args.cov)
            executability_report, action_iteration_report, action_progress_report, action_sequence_length, coverage_report, unresolved_report, deductions_tally = mox.moxecute()
        except Exception as e:
            priny(e)

    sys.exit(0)
