#Source: https://stackoverflow.com/questions/65540523/python-installation-issue-with-adalm-pluto-typeerror
# Import library
import adi
# Create radio object
sdr = adi.Pluto(uri="ip:192.168.2.1")
# Configure properties
sdr.rx_rf_bandwidth = 4000000
# Get data
data = sdr.rx()