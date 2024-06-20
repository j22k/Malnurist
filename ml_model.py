import pandas as pd
from pymongo import MongoClient
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the best model, LabelEncoder, and StandardScaler
best_model = joblib.load('best_model.pkl')
le = joblib.load('label_encoder.pkl')
scaler = joblib.load('scaler.pkl')

def findMal(df, df2):
    label_encoders = {}
    for column in df.columns:
        le = LabelEncoder()
        # Combine df and df2 to fit the encoder with all possible labels
        combined_data = pd.concat([df[column], df2[column]], axis=0)
        le.fit(combined_data)
        label_encoders[column] = le
    
    for column in df.columns:
        le = label_encoders[column]
        # Handle unseen labels by adding them to the LabelEncoder classes
        unseen_labels = set(df[column]) - set(le.classes_)
        if unseen_labels:
            le.classes_ = np.concatenate([le.classes_, list(unseen_labels)])
        df[column] = le.transform(df[column]) + 11

    # Scale the features using the loaded StandardScaler
    df_scaled = scaler.transform(df)

    # Make prediction
    prediction = best_model.predict(df_scaled)
    Ans = "Selected for JME" if prediction[0] == 1 else "Not selected for JME"

    # Add the prediction outcome to the document
    doc['outcome'] = Ans

    # Insert the document into MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.Malnutrition
    collection = db.Datas
    result = collection.insert_one(doc)
    print(f"Inserted document with ID: {result.inserted_id}")

    return Ans
