import streamlit as st
import pickle
import numpy as np

# Load the model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Custom CSS for improved colors and readability
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
        font-family: 'Arial', sans-serif;
    }
    .title-container {
        text-align: center;
        padding: 20px 0;
        color: #2d3436;
    }
    h1 {
        color: #2e8b57;
        font-size: 48px;
        margin-bottom: 10px;
    }
    h2 {
        font-size: 20px;
        color: #34495e;
    }
    .form-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .result-popup {
        padding: 20px;
        background-color: #e8f5e9;
        color: #1b5e20;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("""
<div class="title-container">
    <h1>💻 Laptop Price Prediction App</h1>
    <h2>Estimate the cost of a laptop based on its specifications</h2>
</div>
""", unsafe_allow_html=True)

# Horizontal form layout using columns
with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        company = st.selectbox('💼 Brand', df['Company'].unique())
        type = st.selectbox('📁 Type', df['TypeName'].unique())
        ram = st.selectbox('💾 RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
        weight = st.number_input('⚖️ Weight of the Laptop (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)

    with col2:
        touchscreen = st.selectbox('🔍 Touchscreen', ['No', 'Yes'])
        ips = st.selectbox('🎨 IPS Display', ['No', 'Yes'])
        screen_size = st.slider('📏 Screen size (inches)', 10.0, 18.0, 13.0, step=0.5)
        resolution = st.selectbox('🖥️ Screen Resolution', 
                                  ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', 
                                   '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

    with col3:
        cpu = st.selectbox('💻 CPU', df['Cpu brand'].unique())
        hdd = st.selectbox('📦 HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
        ssd = st.selectbox('💽 SSD (in GB)', [0, 8, 128, 256, 512, 1024])
        gpu = st.selectbox('🎮 GPU', df['Gpu brand'].unique())
        os = st.selectbox('🖥️ Operating System', df['os'].unique())

    # Button to submit inputs
    submitted = st.form_submit_button("🔮 Predict Laptop Price")

if submitted:
    # Calculate Pixels Per Inch (PPI)
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Fixing the variable name for resolution
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

    # Prepare input array for prediction
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os], dtype=object).reshape(1, 12)

    # Predict the price
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    # Display the result with the laptop name
    laptop_name = f"{company} {type}"
    st.markdown(f"""
    <div class="result-popup">
        Predicted Price for {laptop_name} is ₹{predicted_price:,}.
    </div>
    """, unsafe_allow_html=True)
