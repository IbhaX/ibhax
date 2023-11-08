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
    },
    {
        "name": "Biology",
        "description": "Medical Facts"
    },
    {
        "name": "Utility",
        "description": "List of Utility Data"
    }
]

app = FastAPI(
    title="Ibha-X API",
    version="1.0.0",
    description="List of data scraped from various sources formatted into JSON data",
    docs_url="/",
    openapi_tags=tags_metadata,
    contact={
        "name": "Albin Anthony",
        "url": "https://ibhax.github.io/",
        "email": "dp@x-force.example.com"
    }
)


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


@app.get("/fallacy", tags=["Biology"], description="Conspiracies with links for youtube video.")
def fallacies():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/fallacies.json"
    response = requests.get(url).json()
    return response


@app.get("/medical-facts", tags=["Biology"], description="List of Medical Facrs")
def medical_facts():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/medical_facts.json"
    response = requests.get(url).json()
    return response

@app.get("/pincodes", tags=["Utility"], description="List of pincodes with state, district and taluk")
def pincodes():
    url  = "https://raw.githubusercontent.com/IbhaX/json/main/pincodes.json"
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    uvicorn.run(app)
