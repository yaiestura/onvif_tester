import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('onviftester.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

document = db.collection(u'users').document(u'ArtemyMagarin')
doc_ref.set({
    u'first': u'Artemy',
    u'last': u'Magarin',
    u'born': 1998
})
