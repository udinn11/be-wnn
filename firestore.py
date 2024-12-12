from google.cloud import firestore

# Initialize Firestore client
try:
    db = firestore.Client(project="worknonetwork-project", database="waste-not-db")
except Exception as e:
    raise RuntimeError(f"Failed to initialize Firestore client: {e}")

def save_predict(predictions):
    # Pastikan predictions adalah list dan tidak mengandung array dalam array
    if not isinstance(predictions, list):
        raise ValueError("Predictions must be a list")
    
    # Flatten array jika predictions adalah array multidimensi
    flattened_predictions = [item for sublist in predictions for item in (sublist if isinstance(sublist, list) else [sublist])]

    # Format data to save
    data = {
        "predictions": flattened_predictions,  # save predict in list of one dimension
        "created_at": firestore.SERVER_TIMESTAMP 
    }

    # Referensi ke koleksi Firestore
    doc_ref = db.collection("predictions").document()

    try:
        doc_ref.set(data)
        print("Data saved successfully")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")
