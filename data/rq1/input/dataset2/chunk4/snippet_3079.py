#Source: https://stackoverflow.com/questions/63119338/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
acct_deposit = int(act_deposit)

if withdraw > acct_deposit:
    list1.insert(END, ("your balance is low "))

elif acct_deposit > withdraw:
    acct_deposit =  acct_deposit - withdraw