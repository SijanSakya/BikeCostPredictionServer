from flask import Flask, render_template, request, jsonify
from flask import Flask
from flask_cors import CORS
import pandas as pd
import joblib
import pickle
from joblib import dump, load


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# with open('LinearRegressionModel_one.pkl', 'rb') as f:
#     model = pickle.load(f)

model = load("RandomForestModel_one.pkl")

# model = joblib.load("LinearRegressionModel.pkl")
# model2 =pickle.load(open("LinearRegressionModel.pkl"))

@app.route('/')
def home():
    return("hello world")

@app.route('/bike-data', methods=['POST'])  
def receive_data():
    try:
        data = request.json
        bikeName = data['bikeName']
        brand = data['brand']
        city = data['city']
        kmsDriven = int(data['kmsDriven'])
        age = int(data['age'])
        power = int(data['power'])
        owner = int(data['owner'])
    
        print(f"Bike Name: {bikeName}")
        result ={"Bike Name": bikeName ,'Brand' :brand , "City": city , "Kms driven" :kmsDriven,"age": age ,"power":power , "Owner":owner} 
    
   # Construct the input dataframe
        predictions = pd.DataFrame([[bikeName, city, kmsDriven, age, power, brand, owner]],
                                columns=['bike_name', 'city', 'kms_driven', 'age', 'power', 'brand', 'owner'])
        
        # Predict using the model
        prediction = model.predict(predictions)
      
        return jsonify(round(float(prediction[0]), 2))
    
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)



