from google.cloud import firestore

try:
    db = firestore.Client(project="worknonetwork-project")
except Exception as e: 
    raise RuntimeError(f"Failed to initialize Firestore client: {e}")

def save_predict(prediction):
    doc_ref = db.collection('predictions').document()
    doc_ref.set({
        'prediction': prediction,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print("Data stored in Firestore")
