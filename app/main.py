from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

CAT_API_URL = "https://api.thecatapi.com/v1/images/search?breed_ids={}&limit=1"

@app.get("/", response_class=HTMLResponse)
async def home():
    return '''
    <html>
    <head>
        <title>Cat Viewer</title>
    </head>
    <body>
        <h1>Cat Viewer</h1>
        <form action="/get_cat" method="post">
            <label for="catName">Enter Cat Name:</label>
            <input type="text" id="catName" name="catName">
            <button type="submit">Show Cat</button>
        </form>
        <div id="catImageContainer"></div>
    </body>
    </html>
    '''

@app.post("/get_cat", response_class=HTMLResponse)
async def get_cat(cat_name: str = Form(...)):
    breed_id = cat_name
    response = requests.get(CAT_API_URL.format(breed_id))
    data = response.json()
    cat_image_url = data[0]['url']
    return f'''
    <html>
    <head>
        <title>Cat Viewer</title>
    </head>
    <body>
        <h1>Cat Viewer</h1>
        <form action="/get_cat" method="post">
            <label for="catName">Enter Cat Name:</label>
            <input type="text" id="catName" name="catName" value="{cat_name}">
            <button type="submit">Show Cat</button>
        </form>
        <div id="catImageContainer">
            <img src="{cat_image_url}" alt="{cat_name}"/>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
