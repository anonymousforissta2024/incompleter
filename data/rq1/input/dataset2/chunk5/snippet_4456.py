#Source: https://stackoverflow.com/questions/63009994/getting-filenotfounderror
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('json file')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'device-configs').document('5ed7ee5c31ed1b8166e1c2ee')

doc_ref.update({
    u'value.on': True
})