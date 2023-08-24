from flask import Flask, render_template, request, jsonify
from flask import Flask
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)
# CORS(app, origins=["http://localhost:3000/"])

model = joblib.load("LinearRegressionModel.pkl")

@app.route('/')
def home():
    return("hello world");


@app.route('/bike-data', methods=['POST'])
def process_bike_data():
    form_data = request.get_json()
    data = request.json
    print(data)

    # selected_bike = form_data.get('bikeName')
    # selected_brand = form_data.get('brand')
    # selected_city = form_data.get('city')
    # selected_kms_driven = int(form_data.get('kmsDriven'))
    # selected_age = int(form_data.get('age'))
    # selected_power = int(form_data.get('power'))
    # selected_owner = int(form_data.get('owner'))

    # result = f"bikeName:{selected_bike} brand:{selected_brand} kmsDriven:{selected_kms_driven} city:{selected_city} age:{selected_age} power: {selected_power} , owner: {selected_owner} ."

    # input_data = pd.DataFrame([[selected_bike, selected_city, selected_kms_driven, selected_age, selected_power, selected_brand, selected_owner]], columns=['bike_name', 'city', 'kms_driven', 'age', 'power', 'brand', 'owner'])
    # prediction = model.predict(input_data)
    # predicted_price = prediction[0]
    
    # response = {'result': result, 'predicted_price': predicted_price}
    
    # return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
