#Source: https://stackoverflow.com/questions/46237181/type-error-when-using-date-from-a-django-form-i-get-combine-argument-1-must
data1 =collections.OrderedDict()
data1["CashBookEntryData"] = {}
data1["CashBookEntryData"]["Type"] = "FinanceVoucher"
data1["CashBookEntryData"]["CashBookHandle"] = { "Number" : 1 }
data1["CashBookEntryData"]["AccountHandle"] = { "Number" : 5820 },

data1["CashBookEntryData"]["Date"] = my_date,

data1["CashBookEntryData"]["VoucherNumber"] = 100,
data1["CashBookEntryData"]["Text"] = "Dagenssalg",
data1["CashBookEntryData"]["AmountDefaultCurrency"] = 0,
data1["CashBookEntryData"]["CurrencyHandle"] = { "Code" : "DKK" },
data1["CashBookEntryData"]["Amount"] = 9999,
data1["CashBookEntryData"]["DepartmentHandle"] = { "Number" : 1 }