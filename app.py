import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import base64

# Load the model using joblib instead of pickle
model = joblib.load("model.pkl")

# Set page title and favicon
st.set_page_config(page_title="Forest Fire Prediction", page_icon="🔥")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpeg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}

    [data-testid="element-container"] {{
        text-align: center;
        justify-content: center;
        align-items: center;
        height: 100
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the background image

# Define function to display prediction result with emoji
def display_prediction(prediction):
    if prediction == 0:
        return "🔥 Fire Alarm will not ring"
    else:
        return "🚨 Fire Alarm will ring"

# Set title and sidebar
st.title("Forest Fire Prediction 🌲")

# Add sidebar with description
st.sidebar.title("About")
st.sidebar.info(
    "This app predicts the likelihood of a forest fire based on environmental factors."
    " The prediction is made using a machine learning model."
)

# Add input fields for user interaction
st.sidebar.header("User Input")
temperature = st.sidebar.number_input("Temperature [°C]", min_value=-20, max_value=50, value=28)
humidity = st.sidebar.number_input("Humidity [%]", min_value=0, max_value=100, value=45)
tvoc = st.sidebar.number_input("TVOC [ppb]", min_value=0, max_value=600000, value=174)
raw_h2 = st.sidebar.number_input("Raw H2", min_value=10000, max_value=130000, value=12774)
raw_ethanol = st.sidebar.number_input("Raw Ethanol", min_value=15000, max_value=250000, value=20548)
pressure = st.sidebar.number_input("Pressure [hPa]", min_value=900.0, max_value=1000.0, value=937.408)
nc2_5 = st.sidebar.number_input("NC2.5", min_value=0.0, max_value=1000.0, value=0.041)

# Make prediction when button is clicked
if st.sidebar.button("Predict 🔮"):
    # Prepare input data
    input_data = np.array([[temperature, humidity, tvoc, raw_h2, raw_ethanol, pressure, nc2_5]])
    # Make prediction
    prediction = model.predict(input_data)
    # Display prediction result
    st.write(f"## Prediction: {display_prediction(prediction[0])}")

# Add footer
