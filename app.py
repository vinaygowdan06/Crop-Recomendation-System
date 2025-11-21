from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Try loading model and handle error
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    print("Error loading model:", e)
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('index.html', prediction_text="Model not loaded properly.")
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)[0]
        return render_template('index.html', prediction_text=f'Recommended Crop: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
