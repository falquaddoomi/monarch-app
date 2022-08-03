from fastapi import FastAPI, Depends
import requests

from monarch_api.utils.helper import *
from monarch_api import entity, association
import uvicorn

app = FastAPI()
app.include_router(entity.router)
app.include_router(association.router)

base_url = 'http://localhost:8983/solr'


@app.get("/")
async def _root():
    return f"Monarch API - for API documentation, see {base_url}/docs"

@app.get("/api")
async def _api():
    return f"Monarch API - for API documentation, see {base_url}/docs"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
