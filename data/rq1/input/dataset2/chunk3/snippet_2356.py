#Source: https://stackoverflow.com/questions/46237181/type-error-when-using-date-from-a-django-form-i-get-combine-argument-1-must
my_date = (form.cleaned_data['my_date'])
#This comes from a Django form

data2 = {
"CashBookEntryData": {
"Type" : "FinanceVoucher",
"CashBookHandle" : { "Number" : 1 },
"AccountHandle" : { "Number" : 5820 },

"Date" : my_date,

"VoucherNumber" : 100,
"Text" : "Dagenssalg",
"AmountDefaultCurrency" : 0,
"CurrencyHandle" : { "Code" : "DKK" },
"Amount" : beloeb_salg,
"DepartmentHandle" : { "Number" : 1 }
}
}