#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from pkgutil import get_data

@fixture(scope='session')
def ref_o_full():
    return pd.read_csv(StringIO(get_data('test_data', 'ref_o.csv').decode()))