maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)