#Source: https://stackoverflow.com/questions/65181589/python-json-dumps-typeerror-object-of-type-set-is-not-json-serializable-whe
rev_= 'Package ID: bbbbb\nBuild\nnumber: 154\nBuilt\n'
s_ver_str_ = 'bbb.bbb.3.3.98'
result = json.dumps({"rev": rev_, "s_ver_str": s_ver_str_, "pro": {'message': 'no verstion found'}})