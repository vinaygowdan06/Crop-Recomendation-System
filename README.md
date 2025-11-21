🌾 Crop Recommendation System
This project predicts the most suitable crop to grow based on soil nutrients and climatic conditions.
It uses Machine Learning (Random Forest Classifier) to recommend the best crop for a given set of inputs.

📘 About the Project
The system takes soil and weather parameters like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall and predicts the ideal crop.
This project helps in making data-driven agricultural decisions.

🚀 Features
✔️ Machine Learning–based crop prediction
✔️ Flask web application
✔️ Trained model included (model.pkl)
✔️ Uses real agricultural dataset
✔️ User-friendly HTML interface
📂 Project Structure
📁 Crop-Recommendation-System/

│

├── 📁 templates/

│ └── index.html # Web UI (HTML Form for user inputs)

│

├── Crop_recommendation.csv # Dataset used for model training

├── LICENSE # MIT License for your project

├── README.md # Full project documentation

├── app.py # Flask backend (loads model & predicts crop)

├── model.pkl # Trained Random Forest ML model

└── train_model.py # Script to train the ML model and save model.pkl