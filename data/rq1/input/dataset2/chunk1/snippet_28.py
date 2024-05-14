#Source: https://stackoverflow.com/questions/67930156/sending-raw-transaction-from-web3py-typeerror-lambda-missing-4-required-po
t = w3.eth.account.sign_transaction(test_contract.functions.edit("test").buildTransaction(
    {
        "nonce": w3.eth.get_transaction_count(w3.eth.default_account)
    }
), pkey)
w3.eth.send_raw_transaction(t)