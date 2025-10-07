# my main streamlit app- runs the whole app
import streamlit as st
import requests #to send requests to external APIs (OpenWeatherMap)
import os
from dotenv import load_dotenv

#loads the environment variables
load_dotenv() #reads the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY") #gets the API key from that file to keep API key private

st.title("Weather App")
st.write("Enter a city name or zip code to get the current weather.")

location = st.text_input("Location") #whatever the user typed is stored in var 'location'

if st.button("Get Weather"):
  if location: #makes sure the user typed something
    #creates a URL to ge the weather from that location from OpenWeatherMap and sends a GET request to OpenWeatherMaps
    #stores the result in response variable
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

  if response.status_code == 200: #if request succeeded
    data = response.json() #converts the JSON result to a python dictionary
    st.subheader("f"Weather in {data['name']}, {data['sys']['country']}") #city and country
    st.image(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png") #weather icon
    st.write(f"Temperature:** {data['main']['temp']} degrees celcius") #temperature
    st.write(f"**Humidity:** {data['main']['humidity']}%") #humidity
    st.write(f"**Description:** {data['weather'][0]['description'].capitalize()}") #description (starts w/capital letter)
  else:
    st.error("Location not found: Try another city or zip code.") #if API request fails
else:
  st.warning("Please enter a location.") #if request did not succeed
