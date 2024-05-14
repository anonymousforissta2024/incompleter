#Source: https://stackoverflow.com/questions/52920680/dataframe-append-generates-typeerror
import h5py
import numpy as np
import pandas as pd

from datetime import datetime
from os import listdir
from pandas import HDFStore


def maintainLedger(mode, tick, lastBuyy = 0, lastSell = 0, quan = 0, prof = 0):
    """THIS FUNCTION WRITES AND READS TRANSACTION DETAILS.
       mode = 0 - IF FILE EXITS, READ FILE
       mode = 1 - IF FILE EXITS, APPEND TO FILE"""

    # CHECK IF LEDGER FILE EXISTS, IF NOT CREATE A LEDGER FILE FOR THE FIRST TIME
    path = r'ledger'
    suff = r'h5'
    flie = listdir(path)
    flie = [item for item in flie if item.endswith(suff)]

    if len(flie) == 0:
        HDF5Data = HDFStore('ledger/ledger.h5')

        # GENERATE NEW VALUES OF DATE/TIME
        mi = int(datetime.now().minute)
        ho = int(datetime.now().hour)
        da = int(datetime.now().day)
        we = int(datetime.now().isocalendar()[1])
        mo = int(datetime.now().month)
        ye = int(datetime.now().year)

        newwData = np.array([mode, mi, ho, da, we, mo, ye, tick, lastBuyy, lastSell, quan, prof]).reshape(1, 12)
        newwData = pd.DataFrame(newwData, columns = ['mode', 'mi', 'ho', 'da', 'we', 'mo', 'ye', 'tick', 'laBu', 'laSe', 'quan', 'prof'])
        HDF5Data.put('data', newwData, format = 'table', data_columns = True)
        HDF5Data.close()

    elif len(flie) == 1:
        if mode == 0:
            # READ PREVIOUSLY SAVED DATA AS PANDAS DATAFRAME
            readData = pd.read_hdf('ledger/ledger.h5', mode = 'r')

            # DO SOMETHING...

        elif mode == 1:
            # GENERATE NEW VALUES OF DATE/TIME
            mi = int(datetime.now().minute)
            ho = int(datetime.now().hour)
            da = int(datetime.now().day)
            we = int(datetime.now().isocalendar()[1])
            mo = int(datetime.now().month)
            ye = int(datetime.now().year)

            # GATHER NEW DATA INTO NUMPY ARRAY AND CONVERT TO PANDAS DATAFRAME
            newwData = np.array([mode, mi, ho, da, we, mo, ye, tick, lastBuyy, lastSell, quan, prof]).reshape(1, 12)
            newwData = pd.DataFrame(newwData, columns = ['mode', 'mi', 'ho', 'da', 'we', 'mo', 'ye', 'tick', 'laBu', 'laSe', 'quan', 'prof'])

            # READ PREVIOUSLY SAVED DATA AS PANDAS DATAFRAME AND APPEND NEW DATA
            readData = pd.read_hdf('ledger/ledger.h5', mode = 'a')
            readData.append('data', newwData)

            tempData = pd.read_hdf('ledger/ledger.h5', mode = 'r')
            print(tempData)

        else:
            print('Please check input data for errors!')



if __name__ == '__main__':
    maintainLedger(1, "AAPL")