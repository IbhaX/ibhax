import json
import requests
from typing import Optional

from fastapi import FastAPI
import uvicorn
import re
from bs4 import BeautifulSoup


github_url = "https://github.com/IbhaX/json/blob/main/"

result = requests.get(github_url)

soup = BeautifulSoup(result.content, "html.parser")
jsonfiles = soup.find_all(title=re.compile("\.json$"))

filenames = [ ]
for i in jsonfiles:
        filenames.append(i.extract().get_text())


tags_metadata = [
    {
        "name": "Endpoints",
        "description": "List of endpoints"
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


urls = [f"https://raw.githubusercontent.com/IbhaX/json/main/{i}" for i in filenames]


def make_request(url):
    res = requests.get(url)
    return res.json() if res.status_code == 200 else []


def endpoint_factory(endpoint, url):
    @app.get(endpoint, tags=["Endpoints"])
    def world_facts():
        return make_request(url)
    return world_facts


def main():
    for url in urls:
        base = [i for i in url.split("/")[-1].split(".")[0].split("_") if i.isalpha()]
        endpoint = "/" + "-".join(base)
        endpoint_factory(endpoint, url)


main()

if __name__ == "__main__":
    main()
    uvicorn.run(app, port=5000)
