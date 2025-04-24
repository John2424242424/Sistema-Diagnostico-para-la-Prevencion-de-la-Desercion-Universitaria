import firebase_admin

from firebase_admin import credentials, firestore, storage

# Cargar las credenciales de acceso
cred = credentials.Certificate('C:/Users/Sombralis/Documents/Proyecto/credenciales/proyecto-a4c8d-firebase-adminsdk-fbsvc-bd7bbf8f95.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Conexion a Firestore
db = firestore.client()

# Ejemplo: Agregar un documento
#doc_ref = db.collection('usuarios').document('usuario1')
#doc_ref.set({
#    'nombre': 'Juan',
 #   'edad': 30
#})