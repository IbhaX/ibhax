import requests
from typing import Optional

from fastapi import FastAPI
import uvicorn



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ibhax API", "status": "Active"}

@app.get("/items/{item_id}")
def amazing_facts():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/amazing_world_facts.json"
    response = requests.get(url).json()
    return response



if __name__ == "__main__":
    uvicorn.run(app)
