#Source: https://stackoverflow.com/questions/71764549/python-error-attributeerror-enter-using-selenium
from booking.booking import Booking

with Booking() as bot:
    bot.cookies()
    bot.select_place_to_go()