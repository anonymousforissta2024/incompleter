#Source: https://stackoverflow.com/questions/76234608/typeerror-string-indices-must-be-integers-not-str
if __name__ == '__main__':
    _response_text = API('https://api.bitopro.com/v3/provisioning/limitations-and-fees')
    _tradingFeeRateDict = parse(_response_text)
    verify_vip0_twd_volume(_tradingFeeRateDict)