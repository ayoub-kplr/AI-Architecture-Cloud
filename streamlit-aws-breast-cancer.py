import requests
import streamlit as st
import json
# Define the API endpoint URL
api_url = "https://runtime.sagemaker.us-east-1.amazonaws.com/endpoints/DEMO-linear-endpoint-202302131328/invocations"


# Define a function to call the API and return the prediction result
def predict_cancer(input_data):
    response = requests.post(api_url, json=input_data)
    return response.json()

# Define the Streamlit app UI
st.title("Cancer Prediction App")
radius_mean = st.number_input("insert a number for radius mean", step=1)
texture_mean = st.number_input("insert a number for texture mean", step=1)
perimeter_mean = st.number_input("insert a number for perimeter mean", step=1)
area_mean = st.number_input("insert a number for area mean", step=1)
smoothness_mean = st.number_input("insert a number for smothless mean", step=1)
compactness_mean = st.number_input("insert a number for compactness_mean", step=1)
concavity_mean = st.number_input("insert a number for concavity_mean", step=1)
concave_points_mean = st.number_input("insert a number for concave_points_mean", step=1)
symmetry_mean = st.number_input("insert a number for symmetry_mean", step=1)
fractal_dimension_mean = st.number_input("insert a number for fractal_dimension_mean", step=1)
radius_se = st.number_input("insert a number for radius_se", step=1)
texture_se = st.number_input("insert a number for texture_se", step=1)
perimeter_se = st.number_input("insert a number for perimeter_se", step=1)
area_se = st.number_input("insert a number for area_se", step=1)
smoothness_se = st.number_input("insert a number for smoothness_se", step=1)
compactness_se = st.number_input("insert a number for compactness_se", step=1)
concavity_se = st.number_input("insert a number for concavity_se", step=1)
concave_points_se = st.number_input("concave_points_se", step=1)
symmetry_se = st.number_input("insert a number for symmetry_se", step=1)
fractal_dimension_se = st.number_input("insert a number for fractal_dimension_se", step=1)
radius_worst = st.number_input("insert a number for radius_worst", step=1)
texture_worst = st.number_input("insert a number for texture_worst", step=1)
perimeter_worst = st.number_input("insert a number for perimeter_worst", step=1)
area_worst = st.number_input("insert a number for area_worst", step=1)
smoothness_worst = st.number_input("insert a number, for smoothness_worst", step=1)
compactness_worst = st.number_input("insert a number for compactness_worst", step=1)
concavity_worst = st.number_input("insert a number for concavity_worst", step=1)
concave_points_worst = st.number_input("insert a number for concave_points_worst", step=1)
symmetry_worst = st.number_input("insert a number for symmetry_worst", step=1)
fractal_dimension_worst = st.number_input("insert a number for fractal_dimension_worst", step=1)
    

input_data = {
    "radius_mean": radius_mean,
    "texture_mean": texture_mean,
    "perimeter_mean": perimeter_mean,
    "area_mean":area_mean,
    "smoothness_mean":smoothness_mean,
    "compactness_mean":compactness_mean,
    "concavity_mean": concavity_mean,
    "concave_points_mean": concave_points_mean,
    "symmetry_mean": symmetry_mean,
    "fractal_dimension_mean": fractal_dimension_mean,
    "radius_se": radius_se,
    "texture_se": texture_se,
    "perimeter_se": perimeter_se,
    "area_se": area_se,
    "smoothness_se": smoothness_se,
    "compactness_se":compactness_se,
    "concavity_se":concavity_se,
    "concave_points_se": concave_points_se,
    "symmetry_se": symmetry_se,
    "fractal_dimension_se": fractal_dimension_se,
    "radius_worst": radius_worst,
    "texture_worst": texture_worst,
    "perimeter_worst": perimeter_worst,
    "area_worst":area_worst,
    "smoothness_worst":smoothness_worst,
    "compactness_worst": compactness_worst,
    "concavity_worst": concavity_worst,
    "concave_points_worst": concave_points_worst,
    "symmetry_worst": symmetry_worst,
    "fractal_dimension_worst": fractal_dimension_worst,
}

# Convert input_data dictionary to comma-separated string
data_string = ",".join(str(v) for v in input_data.values())

# Create dictionary with "data" key and data_string value
json_data = json.dumps({"data": data_string})




print(json_data)
if st.button("Predict"):
    prediction = predict_cancer(input_data)
    st.write("Prediction:", prediction)
