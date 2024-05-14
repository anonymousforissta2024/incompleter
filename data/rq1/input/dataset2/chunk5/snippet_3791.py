#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - settings.py

import main
import os

URL      = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
DIR      = os.path.dirname(os.path.realpath(__file__))
FILE     = os.path.join(DIR, 'exData.xml')

OPTIONS = {'USD' : main.toUSD, 'JPY' : main.toJPY, 'BGN' : main.toBGN, 'CZK' : main.toCZK,
           'DKK' : main.toDKK, 'GBP' : main.toGBP, 'HUF' : main.toHUF, 'PLN' : main.toPLN,
           'RON' : main.toRON, 'SEK' : main.toSEK, 'CHF' : main.toCHF, 'ISK' : main.toISK,
           'NOK' : main.toNOK
}