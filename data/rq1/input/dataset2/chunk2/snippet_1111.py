#Source: https://stackoverflow.com/questions/57621345/python-typeerror-shows-up-during-ci-cd-process
import pkg_resources

DATA_PATH = 'package.name.data'
MY_DATA_PATH = pkg_resources.resource_filename(DATA_PATH, 'MY_DATA.txt')


def do_some_stuff_with_data(data_path=MY_DATA_PATH):
    ...