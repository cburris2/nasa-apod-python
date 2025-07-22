from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/apod")
def get_apod(key: str | None = None):
    if key:
        api_key = key # Use a real API key from NASA
    else: 
        api_key = "DEMO_KEY"  # Default API key if none provided
    from apod_api import get_apod_data
    return get_apod_data(api_key)   