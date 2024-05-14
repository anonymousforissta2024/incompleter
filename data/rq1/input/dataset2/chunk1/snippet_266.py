#Source: https://stackoverflow.com/questions/57472047/trying-to-connect-hdfs-using-python-client-library-pyarrow-but-getting-error-fil
import pyarrow
import os
import posixpath
import sys

from pyarrow.util import implements
from pyarrow.filesystem import FileSystem
import pyarrow.lib as lib

pyarrow.hdfs.connect(host='xx.xx.xx.xx', port=22, user='cloudera', kerb_ticket=None, driver='libhdfs', extra_conf=None)