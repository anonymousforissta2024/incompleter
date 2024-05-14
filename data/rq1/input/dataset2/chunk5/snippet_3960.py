#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from pkg_resources import resource_filename
from os.path import join as join_path

@fixture(scope='session')
def ref_o_full():
    dir = resource_filename(__name__, 'test_data')
    return pd.read_csv(join_path(dir, 'ref_o.csv'))