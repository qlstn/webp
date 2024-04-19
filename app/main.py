from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=110&bizCd=C&apiKey=VWICH9DPhFOx1x992yQ09VW3jf2jw0mi7P9h96s4&returnType=json"
    
    contents = requests.get(URL).text
    
    return { "message": contents }

@app.get("/home")
def home():
    return { "message": "Home! "}