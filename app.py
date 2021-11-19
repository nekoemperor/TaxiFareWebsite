import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''
d = st.date_input("Pickup date", datetime.date(2021, 11, 19))
st.write('Pickup date:', d)

t = st.time_input('Pickup time', datetime.time(12, 00))
st.write('Pickup time', t)

pickup_longitude = st.number_input('Insert pickup longitude')
st.write('Longitude', pickup_longitude)

dropoff_lattitude = st.number_input('Insert dropoff lattitude')
st.write('Lattitude', dropoff_lattitude)

dropoff_longitude = st.number_input('Insert dropoff longitude')
st.write('Longitude', dropoff_longitude)

pickup_lattitude = st.number_input('Insert pickup lattitude')
st.write('Lattitude', pickup_lattitude)

passenger_count = st.number_input('Insert number of passengers')
st.write('Passengers', passenger_count)

url = 'https://taxifare.lewagon.ai/predict'

params = dict(pickup_datetime=f'{d} {t}',
              pickup_longitude=pickup_longitude,
              pickup_latitude=pickup_lattitude,
              dropoff_longitude=dropoff_longitude,
              dropoff_latitude=dropoff_lattitude,
              passenger_count=int(passenger_count))

response = requests.get(url, params=params)

if response.status_code == 200:
    print("API call success")
else:
    print(response.status_code)

st.write(response.json())
