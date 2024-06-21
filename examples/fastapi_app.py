from fastapi import FastAPI
from starlette.config import Config
from umami_analytics.middleware import UmamiMiddleware

config = Config()
UMAMI_API_ENDPOINT = config('UMAMI_API_ENDPOINT')
UMAMI_API_TOKEN = config('UMAMI_API_TOKEN')
UMAMI_SITE_ID = config('UMAMI_SITE_ID')

print(f"UMAMI_API_ENDPOINT: {UMAMI_API_ENDPOINT}")

app = FastAPI()

app.add_middleware(UmamiMiddleware, api_endpoint=UMAMI_API_ENDPOINT, token=UMAMI_API_TOKEN, website_id=UMAMI_SITE_ID)


@app.get("/")
async def homepage():
    return {"hello": "world"}


@app.get("/feed")
async def feed():
    return {"posts": []}
