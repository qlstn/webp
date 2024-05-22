from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

import requests

app = FastAPI()

#종의 정보를 받아옴
def get_breeds():
    URL = "https://api.thecatapi.com/v1/breeds?api_key=live_oQmRa1nyv45JtYFmRn7onvEI41iwaBhZZnPZDopjHO5qoAuq7J7fpVKcC4606QrG"
    response = requests.get(URL)
    return response.json() 


@app.get("/", response_class=HTMLResponse)
def root():
    breeds = get_breeds()
    breed_options = "".join([f'<option value="{breed["id"]}">{breed["name"]}</option>' for breed in breeds])
    return f"""
    <html>
        <head>
            <title>고양이 종 검색</title>
        </head>
        <body>
            <form action="/search" method="post">
                <label for="breed">고양이 종을 선택하세요:</label><br>
                <select id="breed" name="breed">
                    {breed_options}
                </select><br>
                <button type="submit">검색</button>
            </form>
        </body>
    </html>
    """
    
@app.post("/search")
def search(breed: str = Form(...)):
    URL = f"https://api.thecatapi.com/v1/images/search?limit=5&breed_ids={breed}&api_key=live_oQmRa1nyv45JtYFmRn7onvEI41iwaBhZZnPZDopjHO5qoAuq7J7fpVKcC4606QrG"
    
    images_response = requests.get(URL)
    
    if images_response.status_code == 200:
        images_data = images_response.json()
        image_urls = [image["url"] for image in images_data]
        
        images_html = "".join([f'<img src="{url}" width="300" height="auto">' for url in image_urls])
        
        return HTMLResponse(content=f"<html><body>{images_html}</body></html>", status_code=200)
    else:
        return {"error": "Failed to fetch images"}