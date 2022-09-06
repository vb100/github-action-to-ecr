import uvicorn
from fastapi import FastAPI
from variables import WeatherVariables
import numpy
import pickle
import pandas as pd
import onnxruntime as rt

# Create application object
app = FastAPI()

# Load model data scaler
pickle_in = open('artifacts/model-scaler.pkl', 'rb')
scaler = pickle.load(pickle_in)

# Load the model
sess = rt.InferenceSession('artifacts/svc.onnx')
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

# API endpoints
@app.get('/')
def index():
	return {'Hello': 'Welcome to the Weather application (v1)!'}

@app.post('/predict')
def predict_weather(data: WeatherVariables):
	data = data.dict()

	# fetch input data using data variables
	temp_c = data['temp_c']
	humidity = data['humidity']
	wind_speed_kmph = data['wind_speed_kmph']
	wind_bearing_degree = data['wind_bearing_degree']
	visibility = data['visibility_km']
	pressure_milibars = data['pressure_milibars']
	current_weather_condition = data['current_weather_condition']

	data_to_pred = numpy.array(
		[[temp_c, humidity, wind_speed_kmph, wind_bearing_degree,
		  visibility, pressure_milibars, current_weather_condition]]
		)

	# Scale the input data
	data_to_pred = scaler.fit_transform(data_to_pred.reshape(1, 7))

	# Model inference
	prediction = sess.run(
		[label_name], {input_name: data_to_pred.astype(numpy.float32)}
		)[0]

	if (prediction[0] > 0.5):
		prediction = 'Rain'
	else:
		prediction = 'No_rain'

	return {'prediction': prediction}
