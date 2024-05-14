#Source: https://stackoverflow.com/questions/75198341/filenotfounderror-errno-2-no-such-file-or-directory-sp500-stocks-csv
import errno
import os

raise FileNotFoundError(
    errno.ENOENT, os.strerror(errno.ENOENT), 'sp500_stocks.csv')