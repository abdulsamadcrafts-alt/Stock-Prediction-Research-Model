This project is a deep learning-based stock price prediction model using Long Short-Term Memory (LSTM) networks. The model is trained on historical stock data for Google and Apple to predict future stock prices based on past trends.

The main objective of this project is to study how the lookback window (number of past days used for prediction) affects model accuracy.

📊 Dataset
The dataset contains historical stock market data with the following features:

Date
Open
High
Low
Close
Volume
Two datasets were used:

Google stock data (2012–2016)
Apple stock data (2020–2026)
🧠 Model Architecture
The model is built using a stacked LSTM architecture:

4 LSTM layers (50 units each)
Dropout layers (0.2) to reduce overfitting
Dense output layer (1 unit)
Optimizer: Adam
Loss Function: Mean Squared Error (MSE)
⏳ Lookback Window Experiment
The key experiment in this project is testing different values of PAST_DAYS:

30 days
60 days
90 days
120 days
150 days
📈 Results:
30 days gave the best accuracy
Performance decreased as lookback window increased
Larger windows introduced noise and reduced model focus on recent trends
⚙️ Technologies Used
Python
NumPy
Pandas
Matplotlib
TensorFlow / Keras
Scikit-learn
Joblib
🚀 How It Works
Load and preprocess stock price data
Normalize data using MinMaxScaler
Create time-series sequences using past N days
Train LSTM model on sequences
Predict future stock prices
Compare predicted vs real values using plots
📉 Output
The model generates visual plots comparing:

Actual stock prices
Predicted stock prices
📌 Key Insight
This project demonstrates that in time-series forecasting, selecting the correct lookback window is crucial. A smaller window (30 days) performed better than larger ones, showing that recent trends are more important than long historical patterns for this dataset.

📂 Project Structure
├── Google_Stock_Price_Train.csv ├── Google_Stock_Price_Test.csv ├── Apple_Stock_Clean.csv ├── Apple_Stock_Price_Test.csv ├── model.py ├── regressor.pkl └── README.md

📜 Author
Developed by: Abdul Samad Abed Qureshi And Mohammed Fouzaan Shakeel
⚠️ Disclaimer
This project is for educational purposes only and should not be used for real financial trading decisions.