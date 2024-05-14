#Source: https://stackoverflow.com/questions/69187685/getting-attributeerror-module-base64-has-no-attribute-decodestring-error-wh
from ldif3 import LDIFParser

parser = LDIFParser(open('dse3.ldif', 'rb'))
for dn, entry in parser.parse():
    if dn == "cn=Schema Compatibility,cn=plugins,cn=config":
        if entry['nsslapd-pluginEnabled'] == ['on']:
            print('Entry record: %s' % dn)