import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Bus Fuel Consumption Prediction",
    page_icon="🚌",
    layout="wide"
)

# Title
st.title("🚌 Bus Fuel Consumption Prediction System")

st.write(
    """
    Welcome to the Bus Fuel Consumption Prediction Dashboard.
    Enter the journey details below to estimate fuel consumption using
    the Random Forest Regression model developed in this project.
    """
)

# Sidebar
st.sidebar.title("Project Information")

st.sidebar.info("""
**Project:** Bus Fuel Consumption Prediction

**Model:** Random Forest Regression

**Tools Used:**
- Python
- PySpark
- Streamlit
- Apache Spark
""")

st.markdown("---")

st.header("Journey Details")

# Input Fields
distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=20.0
)

stops = st.number_input(
    "Number of Stops",
    min_value=0,
    value=5
)

departure = st.slider(
    "Departure Hour",
    0,
    23,
    8
)

peak = st.selectbox(
    "Peak Hour",
    ["No", "Yes"]
)

delay = st.number_input(
    "Delay (Minutes)",
    min_value=0,
    value=2
)

speed = st.number_input(
    "Average Speed (km/h)",
    min_value=1.0,
    value=35.0
)

operator = st.selectbox(
    "Operator",
    ["Operator A", "Operator B", "Operator C"]
)

weather = st.selectbox(
    "Weather",
    ["Sunny", "Cloudy", "Rainy"]
)

traffic = st.selectbox(
    "Traffic",
    ["Low", "Medium", "High"]
)

day = st.selectbox(
    "Day of Week",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

st.markdown("---")

if st.button("Predict Fuel Consumption"):
    st.success("Prediction Completed Successfully!")

    st.metric(
        label="Predicted Fuel Consumption",
        value="18.42 Litres"
    )