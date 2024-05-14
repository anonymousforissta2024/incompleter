#Source: https://stackoverflow.com/questions/57395187/python-string-concatenation-typeerror-bad-operand-type-for-unary-str
weather = forecast('api_key',lat, -long)
windbearing = weather.windBearing
windspeed = float(weather.windSpeed)

def windcompass(windbearing):
    val = int((windbearing/22.5)+.5)
    argument = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return argument[(val % 16)]

direction = windcompass(windbearing)

print('The wind is blowing ', + windspeed, + 'at ', + direction, + 'MPH')