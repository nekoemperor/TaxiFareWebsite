import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
'''
# NY TaxiFareModel
'''

d = st.date_input("Pickup date", datetime.date(2021, 11, 8))
st.write('Pickup date:', d)

t = st.time_input('Pickup time', datetime.time(12, 00))
st.write('Pickup time', t)

pickup_longitude = st.number_input('Insert pickup longitude', float(-73.950655))
st.write('Longitude', pickup_longitude)

pickup_latitude = st.number_input('Insert pickup latitude', float(40.783282))
st.write('Lattitude', pickup_latitude)

dropoff_longitude = st.number_input('Insert dropoff longitude',
                                    float(-73.984365))
st.write('Longitude', dropoff_longitude)

dropoff_latitude = st.number_input('Insert dropoff latitude', float(40.769802))
st.write('Lattitude', dropoff_latitude)

passenger_count = st.number_input('Insert number of passengers', float(1.00))
st.write('Passengers', passenger_count)

url = 'https://taxifare.lewagon.ai/predict'

params = dict(
    pickup_datetime=f'{d} {t}',
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=int(passenger_count)
    )

response = requests.get(url, params=params)

if response.status_code == 200:
    print("API call success")
else:
    print(response.status_code)

st.write(response.json())
