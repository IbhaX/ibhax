import json
import requests
from typing import Optional

from fastapi import FastAPI
import uvicorn


tags_metadata = [
    {
        "name": "Status",
        "description": "Health Check - Status of the API Server"
    },
    {
        "name": "Facts",
        "description": "All kinds of Amazing Facts"
    },
    {
        "name": "Conspiracy",
        "description": "Conspiracy world-wide"
    }
]

app = FastAPI(docs_url="/", openapi_tags=tags_metadata)


@app.get("/status", tags=["Status"], description="Checks status of the API server. Just returns status = Active")
async def root():
    return {"status": "Active"}


@app.get("/world-facts", tags=["Facts"], description="Amazing world facts with images")
def world_facts():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/amazing_world_facts.json"
    response = requests.get(url).json()
    return response


@app.get("/amazing-facts", tags=["Facts"], description="Amazing facts")
def amazing_facts():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/amazing_facts_128.json"
    response = requests.get(url).json()
    return response


@app.get("/awesome-facts", tags=["Facts"], description="Awesome facts")
def awesome_facts():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/awesome_facts.json"
    response = requests.get(url).json()
    return response


@app.get("/conspiracy", tags=["Conspiracy"], description="Conspiracies with links for youtube video.")
def conspiracies():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/conspiracies.json"
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    uvicorn.run(app)
