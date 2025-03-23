#### ***Task-Objective
This project aims to predict car sales using historical data and machine learning techniques. The core predictive model is built using Linear Regression to estimate sales figures based on various car attributes and market factors. The solution is deployed as a web application using Streamlit, allowing users to interact with the model in real time.


## **🔧 Setup & Run the Project**
Follow these steps to set up and run the project on your local machine.


### **1️⃣ Create a Virtual Environment (Recommended)**
A virtual environment helps manage dependencies for the project.

# Create a virtual environment
python -m venv my_venv

# Activate the virtual environment:
# Windows:
my_venv\Scripts\activate

# Mac/Linux:
source my_venv/bin/activate



### **2️⃣ Install Required Libraries

# Ensure you have all necessary dependencies installed.
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib



### **3️⃣ Run the Jupyter Notebook

# Train the machine learning model using Jupyter Notebook.
# Install Jupyter (if not installed)
pip install notebook

# Start Jupyter Notebook
jupyter notebook

 
# Open the notebook (Car_Sales_Prediction.ipynb).

# Run all cells to train and evaluate the model.

# Save the trained model using joblib.dump(model, "model.pkl").


### **4️⃣ Run the Streamlit Web App
# Once the model is trained, launch the Streamlit web app.

streamlit run app.py

The app should open in your browser at http://localhost:8501/.

Enter car details (e.g., Year, Mileage, Price) and get predictions.

## 📌 Features
✅ Predicts car sales based on input features.
✅ Built with Linear Regression for accurate predictions.
✅ User-friendly web interface using Streamlit.
✅ Supports real-time input & visualization.









