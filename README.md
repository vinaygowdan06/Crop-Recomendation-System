# 🌾 Crop Recommendation System

This project predicts the most suitable crop to grow based on soil nutrients and climatic conditions.  
It uses a **Machine Learning Random Forest Classifier** to recommend the best crop for given input parameters.

---

## 📘 About the Project

The system takes soil and weather parameters — **Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, rainfall** — and predicts the ideal crop.  
It helps farmers and students make accurate, data-driven agricultural decisions.

---

## 🚀 Features

- ✔ Machine Learning–based crop prediction  
- ✔ Flask web application  
- ✔ Trained model included (`model.pkl`)  
- ✔ Real agricultural dataset  
- ✔ Clean HTML UI (`templates/index.html`)

---

## 📂 Project Structure

Crop-Recommendation-System/
├── templates/
│ └── index.html # HTML form for inputs
├── Crop_recommendation.csv
├── LICENSE
├── README.md
├── app.py # Flask backend
├── model.pkl # Trained Random Forest model
└── train_model.py # Training script


---

## 🧪 Input Parameters

| Parameter | Description |
|----------|-------------|
| N | Nitrogen |
| P | Phosphorus |
| K | Potassium |
| Temperature | °C |
| Humidity | % |
| pH | Soil pH |
| Rainfall | mm |

---

## 🛠 Tech Stack

- Python  
- Flask  
- Scikit-Learn  
- Pandas  
- NumPy  

---

## ▶️ How to Run the Project

### 1. Create virtual environment (optional but recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

3. Run the Flask App
python app.py

4. Open in Browser
http://127.0.0.1:5000/

5. Train the Model
To retrain the model:python train_model.py
