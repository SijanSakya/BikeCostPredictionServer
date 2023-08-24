from flask import Flask, render_template, request, jsonify
from flask import Flask
from flask_cors import CORS
import pandas as pd
import joblib
import pickle

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = joblib.load("LinearRegressionModel.pkl")
# model2 =pickle.load(open("LinearRegressionModel.pkl"))

@app.route('/')
def home():
    return("hello world")

@app.route('/bike-data', methods=['POST'])
def receive_data():
    data = request.json
    bike_name = data['bikeName']
    brand = data['brand']
    city = data['city']
    kms_driven = int(data['kmsDriven'])
    age = int(data['age'])
    power = int(data['power'])
    owner = int(data['owner'])
    
    print(f"Bike Name: {bike_name}")
    result ={"Bike Name": bike_name ,'Brand' :brand , "City": city , "Kms driven" :kms_driven,"age": age ,"power":power , "Owner":owner} 
    
   # Construct the input dataframe
    predictions = model.predict(pd.DataFrame([[bike_name, city, kms_driven, age, power, brand, owner]], 
                                                columns=['bike_name','city','kms_driven','age','power','brand','owner']))
        
# Predict using the model
    prediction = model.predict(predictions[0])
        
 # Return prediction
    return jsonify({"predicted_value": predictions[0]})
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)
