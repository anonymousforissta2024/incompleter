#Source: https://stackoverflow.com/questions/71188328/typeerror-nonetype-object-is-not-subscriptable-python3
if 0 < i < noSteps:
    order = (client.LinearOrder.LinearOrder_new(side=side, symbol="BTCUSDT", order_type="Limit",
                                                qty=allocatedQuantities[i], price=priceArray[i],
                                                time_in_force="GoodTillCancel",
                                                reduce_only=False, close_on_trigger=False,
                                                take_profit=takeProfits[i]).result())
    print(order)
    temp_order = order[0]['result']['order_id']
    ordersArray.append(temp_order)