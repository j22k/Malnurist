from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import pandas as pd
from ml_model import findMal

app = Flask(__name__)

# Check MongoDB connection status
def check_mongo_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Malnutrition
        names = db.list_collection_names()
        print("Connected Successfully", names)
    except Exception as e:
        print(f"Failed to connect to MongoDB: {str(e)}")
        
check_mongo_connection()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    try:
        print("tst1")
        data = {
            'Country Short Name': request.form.get('Country Short Name'),
            'Year period': request.form.get('Year period'),
            'Median Year': request.form.get('Median Year'),
            'Start Month': request.form.get('Start Month'),
            'End Month': request.form.get('End Month'),
            'Age': request.form.get('Age'),
            'Sex': request.form.get('Sex'),
            'MUAC(IN)': request.form.get('MUAC(IN)'),
            'WHZ': request.form.get('WHZ'),
            'Weight(kg)': request.form.get('Weight(kg)'),
            'Height(in)': request.form.get('Height(in)'),
            'Head Circumference(cm)': request.form.get('Head Circumference(cm)')
        }
        print("tst2")
        data2 = {
            'Name': request.form.get('Name'),
            'Father Name': request.form.get('Father Name'),
            'Mother Name': request.form.get('Mother Name'),
            'Ration Card No': request.form.get('Ration Card No'),
            'Pincode': request.form.get('Pincode'),
            'Health Center No': request.form.get('Health Center No')
        }
        df = pd.DataFrame([data])
        df2 = pd.DataFrame([data2])
        print("tst3")
        res = findMal(df, df2)
        print("tst3")
        return jsonify(res)
    except Exception as e:
        app.logger.error(f'Exception on /find: {e}')
        return jsonify({'error': str(e)}), 500

@app.route('/Show')
def Show():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.Malnutrition
    collection = db.Datas
    data_from_mongo = list(collection.find({}, {'_id': 0}))
    df = pd.DataFrame(data_from_mongo)
    return render_template('view_datas.html', data=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=False)
