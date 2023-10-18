import requests
import json
import pandas as pd

lat= input("Enter the lat ")
long= input("Enter the long ")

url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"

r=requests.get(url)

print(r.text)
wdic=json.loads(r.text)

print("Time_stamp",wdic['hourly']['time'][-1],"\nTemp",wdic["hourly"]["temperature_2m"][-1])