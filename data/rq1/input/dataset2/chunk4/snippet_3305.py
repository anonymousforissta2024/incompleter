#Source: https://stackoverflow.com/questions/74933471/type-error-and-got-an-unexpected-keyword-argument-when-passing-dict-to-python-z
from zeep.wsse.signature import BinarySignature
from zeep.wsse import utils
from datetime import datetime, timedelta
import contextlib
import os
import requests
from requests_pkcs12 import Pkcs12Adapter
from zeep.transports import Transport
from zeep import Client, Settings
from pathlib import Path
from tempfile import NamedTemporaryFile
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
import random
import logging.config

# USE THE MOST VERBOSE LOGGING LEVEL
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})


class BinarySignatureTimestamp(BinarySignature):
    def apply(self, envelope, headers):
        security = utils.get_security_header(envelope)

        created = datetime.utcnow()
        expired = created + timedelta(seconds=1 * 60)

        timestamp = utils.WSU('Timestamp')
        timestamp.append(utils.WSU('Created', created.replace(microsecond=0).isoformat() + 'Z'))
        timestamp.append(utils.WSU('Expires', expired.replace(microsecond=0).isoformat() + 'Z'))

        security.append(timestamp)

        super().apply(envelope, headers)
        return envelope, headers

    def verify(self, envelope):
        return envelope


@contextlib.contextmanager
def pfx_to_pem(pfx_path, pfx_password):
    ''' Decrypts the .pfx file to be used with requests. '''
    pfx = Path(pfx_path).read_bytes()
    private_key, main_cert, add_certs = load_key_and_certificates(pfx, pfx_password.encode('utf-8'), None)

    with NamedTemporaryFile(suffix='.pem', delete=False) as t_pem:
        with open(t_pem.name, 'wb') as pem_file:
            pem_file.write(private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))
            pem_file.write(main_cert.public_bytes(Encoding.PEM))
            for ca in add_certs:
                pem_file.write(ca.public_bytes(Encoding.PEM))
        yield t_pem.name


def generate_nonce(length=15):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


# CERTIFICATES PATHS

api_p12_key = os.path.join('C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.p12')
api_certificate = os.path.join('C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\OSITCC.crt')
api_pfx_key = os.path.join('C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.pfx')

# SETUP
wsdl_file = os.path.join('C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\Nodal.wsdl')

api_base_url = "https://testmisapi.ercot.com"
session = requests.Session()
session.mount(api_base_url,
              Pkcs12Adapter(pkcs12_filename=api_p12_key, pkcs12_password='HIDDEN'))
session.verify = None

transport = Transport(session=session)
settings = Settings(forbid_entities=False)

# CREATE CLIENT
print("Creating client.")
with pfx_to_pem(pfx_path=api_pfx_key, pfx_password='AEP') as pem_fle:
    client = Client(wsdl=wsdl_file, settings=settings, transport=transport,
                    wsse=BinarySignatureTimestamp(pem_fle, api_certificate, "AEP"))

print("Making request.")
request_data = {'http://www.ercot.com/schema/2007-06/nodal/ews/message:RequestMessage': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Header': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Verb': 'create', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Noun': 'OutageSet', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:ReplayDetection': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Nonce': '72465', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Created': '2022-12-27T00:40:00-07:00'}, 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Revision': '004', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Source': 'TAEPTC', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:UserID': 'API_OutplanOSITCC'}, 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Payload': {'http://www.ercot.com/schema/2007-06/nodal/ews:OutageSet': {'http://www.ercot.com/schema/2007-06/nodal/ews:Outage': {'http://www.ercot.com/schema/2007-06/nodal/ews:OutageInfo': {'http://www.ercot.com/schema/2007-06/nodal/ews:outageType': 'PL', 'http://www.ercot.com/schema/2007-06/nodal/ews:Requestor': {'http://www.ercot.com/schema/2007-06/nodal/ews:name': 'API_OutplanOSITCC', 'http://www.ercot.com/schema/2007-06/nodal/ews:userFullName': 'APIOutplanOSITCC'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:Disclaimer': 'tempdisclaimer', 'http://www.ercot.com/schema/2007-06/nodal/ews:disclaimerAck': 'true'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:TransmissionOutage': {'http://www.ercot.com/schema/2007-06/nodal/ews:operatingCompany': 'TAEPTC', 'http://www.ercot.com/schema/2007-06/nodal/ews:equipmentName': '1589', 'http://www.ercot.com/schema/2007-06/nodal/ews:equipmentIdentifier': '_{072D6FCA-D121-49E7-AC9D-CDF5D4DB3D70}', 'http://www.ercot.com/schema/2007-06/nodal/ews:transmissionType': 'DSC', 'http://www.ercot.com/schema/2007-06/nodal/ews:fromStation': 'AIRLINE', 'http://www.ercot.com/schema/2007-06/nodal/ews:outageState': 'O', 'http://www.ercot.com/schema/2007-06/nodal/ews:emergencyRestorationTime': '1', 'http://www.ercot.com/schema/2007-06/nodal/ews:natureOfWork': 'OE'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:Schedule': {'http://www.ercot.com/schema/2007-06/nodal/ews:plannedStart': '2023-01-16T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:plannedEnd': '2023-01-17T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:earliestStart': '2023-01-16T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:latestEnd': '2023-01-17T12:00:00'}}}}}}

print("Call URL")
print(client.service.MarketTransactions(**request_data))