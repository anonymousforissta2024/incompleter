#Source: https://stackoverflow.com/questions/52184713/python3-typeerror-can-only-concatenate-list-not-str-to-list
vat = invoice.partner_id.vat or ''
vat = list(filter(lambda x: x.isnumeric(), vat[:2])) + vat[2:]