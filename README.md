---

# **Laptop Price Prediction Application 💻**

## **Overview**
This project is a web-based application that predicts the price of a laptop based on user-defined specifications such as brand, CPU, RAM, storage, and screen size. The application is built using **Streamlit** and powered by a pre-trained **machine learning model**.

---

## **Technologies Used**
- **Python**: Core programming language  
- **scikit-learn**: For training the machine learning model  
- **Streamlit**: For the interactive web interface  
- **Pandas & Numpy**: For data manipulation and handling  
- **XGBoost**: For model optimization  

---

## **Project Structure**
```
📂 Laptop-Price-Prediction-App/
├── app.py              # Streamlit application code
├── pipe.pkl            # Trained machine learning pipeline
├── df.pkl              # Dataframe used for dropdown references
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
```

---

## **Getting Started**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/mishaelsathe/Laptop-Price-Prediction-Application.git
   cd Laptop-Price-Prediction-Application
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # Mac/Linux  
   .\env\Scripts\activate   # Windows  
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## **How It Works**
1. The user selects laptop specifications using a form interface.
2. The **trained model** predicts the price based on the input features.
3. The prediction is displayed, along with details about the selected configuration.

---

## **Future Improvements**
- Expand the dataset with more laptop configurations.
- Add new features like battery life, graphics performance, etc.
- Improve prediction accuracy by fine-tuning the model.

---

## **License**
This project is licensed under the **MIT License**.

---
