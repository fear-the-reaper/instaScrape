from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

# Importing models
from models.scrape_request import ScrapeRequest

from scrape import scrape_comments

# to handle CORS errorss
origins = ["*"]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=["*"]
    )
]

app = FastAPI(middleware=middleware)

@app.post("/scrape")
def scrape(scrape_req: ScrapeRequest):
    print("Got the request!")
    print(f"url to scrape {scrape_req.url}")
    try:
        url_to_scrape = scrape_req.url
        scraped_comments = scrape_comments(url_to_scrape)
        if len(scraped_comments) > 0:
            return scraped_comments
        return None
    except Exception as e:
        raise HTTPException(500, str(e))