#Source: https://stackoverflow.com/questions/35820418/compound-function-typeerror-int-object-is-not-iterable
# Here is the market
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_total_value(food):
    total = 0
    for items in food:
        while sum(stock[items]) != 0:       #error is on this line
            if stock[items] != 0:
                total += prices[items]
                stock[items] -= 1
            else:
                continue
        if sum(stock[items]) == 0:
            break
    return total

market_items = ["banana", "orange", "apple", "pear"]

total_market_value = compute_total_value(market_items)

print (total_market_value)