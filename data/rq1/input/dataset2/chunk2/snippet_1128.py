#Source: https://stackoverflow.com/questions/53344078/getting-a-typeerror-with-python-quandl-get-raise-on-status
import quandl

data = quandl.get("EIA/PET_RWTC_D")
print(data.head())