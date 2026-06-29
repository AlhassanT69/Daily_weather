import os
import requests
import twilio
import pandas as pd
from twilio.rest import Client

# cities=pd.read_csv("cities.csv")
cities = [
    {"city": "Gamasa", "lat": 31.440392, "lon": 31.54776},
    {"city": "Mansoura", "lat": 31.040703, "lon": 31.358063}
]


account_sid=os.environ.get("TWILIO_ACCOUNT_SID")
auth_tokens=os.environ.get("TWILIO_AUTH_TOKEN")
api_key=os.environ.get("WEATHER_API_KEY")
for city in cities:
    parameters={
        "lat":city["lat"],
        "lon":city["lon"],
        "appid":api_key
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
    response.raise_for_status()
    main_weather=response.json()["weather"][0]["main"]
    description = response.json()["weather"][0]["description"]


    client=Client(account_sid,auth_tokens)
    message = client.messages.create(
        body=f"The weather in {city['city']} is {main_weather}\n"
             f"Description:{description }",
        from_='whatsapp:+14155238886',
        to='whatsapp:+201113337224'
    )
    print(message.status)





