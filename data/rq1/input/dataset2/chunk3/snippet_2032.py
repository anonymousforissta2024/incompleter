#Source: https://stackoverflow.com/questions/68136084/long-list-creating-sorted-typeerror-nonetype-object-is-not-subscriptable
option_list = sorted(option_list, key = lambda option: option['expiration_date'])
option_list = sorted(option_list, key = lambda option: option['strike_price'], reverse=True)