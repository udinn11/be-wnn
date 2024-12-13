from google.cloud import firestore

try:
    db = firestore.Client(project="worknonetwork-project", database="waste-not-db")
except Exception as e:
    raise RuntimeError(f"Failed to initialize Firestore client: {e}")

def save_predict(predictions):
    if not isinstance(predictions, list):
        raise ValueError("Predictions must be a list")
    
    flattened_predictions = [
        item for sublist 
        in predictions for item 
        in (sublist 
            if isinstance(sublist, list) 
            else [sublist])
    ]

    data = {
        "predictions": flattened_predictions,
        "created_at": firestore.SERVER_TIMESTAMP 
    }

    doc_ref = db.collection("predictions").document()

    try:
        doc_ref.set(data)
        print("Data saved successfully")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")
