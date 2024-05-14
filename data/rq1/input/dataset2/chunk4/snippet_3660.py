#Source: https://stackoverflow.com/questions/56333685/typeerror-unhashable-type-set-in-http-get-request
def getInvoice(inv_id):
    response = requests.get("https://api.example.com/invoices/"+str(inv_id)+"?access_token=123456789").json()
    return response

print(getInvoice("5b5f60384b3f"))