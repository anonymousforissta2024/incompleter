#Source: https://stackoverflow.com/questions/59157372/python3-azure-key-vault-keys-creating-ras-key-typeerror
rsa_key = key_client.create_rsa_key("rsa-key-demo", size=2048)
print(rsa_key.name)
print(rsa_key.key_type)