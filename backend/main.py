# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas import Schemas
from dotenv import load_dotenv
from shorten.shorten import Shortener
from db.links import LinksDB


# ---------------------------------------------------------------------------- #
# --- App Configuration ------------------------------------------------------ #
# ---------------------------------------------------------------------------- #

load_dotenv()
schemas = Schemas()
shortener = Shortener()
db = LinksDB()

TAGS_METADATA = [
    {
        "name": "Testing",
        "description": "Routes to test functionality.",
        "externalDocs": {
            "description": "FastAPI Documentation",
            "url": "https://fastapi.tiangolo.com/",
        }
    },
    {
        "name": "Links",
        "description": "Routes to shorten links, save and retrieve it.",
        "externalDocs": {
            "description": "Cuttly documentation",
            "url": "https://cutt.ly/api-documentation/regular-api",
        }
    },
]


# Configure the API with detailed description
app = FastAPI(
    title="Shortener Backend",
    description="URL Shortener with cutt.ly",
    version="0.0.1",
    terms_of_service="https://vanillauys.vercel.app/about",
    contact={
        "name": "Wihan Uys",
        "url": "https://vanillauys.vercel.app/about",
        "email": "wihan@duck.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://spdx.org/licenses/MIT.html",
    },
    root_path="/api",
    openapi_tags=TAGS_METADATA,
    openapi_url="/openapi.json",
)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------- #
# --- Basic API Route -------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


@app.get('/', tags=['Testing'],
    response_model=schemas.Detail,
    responses={
        500: {"model": schemas.Detail}
    }
)
def info():
    """
    ### Basic route to test functionality.
    """
    response = {
        'detail': "view /docs for documentation."
    }
    return JSONResponse(status_code=200, content=response)


# ---------------------------------------------------------------------------- #
# --- Shortener API Routes --------------------------------------------------- #
# ---------------------------------------------------------------------------- #


@app.post('/shorten', tags=['Links'],
    response_model=schemas.Link,
    responses={
        400: {"model": schemas.Detail},
        401: {"model": schemas.Detail},
        409: {"model": schemas.Detail},
        429: {"model": schemas.Detail},
        500: {"model": schemas.Detail},
    }
)
async def shorten(shorten: schemas.ShortenLink):
    """
    ### To shorten a link
    """
    code, response = await shortener.shorten_link(shorten.url)
    return JSONResponse(status_code=code, content=response)


@app.post('/create', tags=['Links'],
    response_model=schemas.Detail,
    responses={
        500: {"model": schemas.Detail},
    }
)
def create(link: schemas.Link):
    """
    ### Save a shortened link.
    """
    code, response = db.create_link(link)
    return JSONResponse(status_code=code, content=response)


@app.get('/get', tags=['Links'],
    response_model=list[schemas.Link],
    responses={
        500: {"model": schemas.Detail},
    }
)
def get():
    """
    ### Get all saved links.
    """
    code, response = db.get_all()
    return JSONResponse(status_code=code, content=response)


@app.delete('/delete', tags=['Links'],
    response_model=schemas.Detail,
    responses={
        500: {"model": schemas.Detail},
    }
)
def delete(key: str):
    """
    ### Delete a saved link.
    """
    code, response = db.delete_link(key)
    return JSONResponse(status_code=code, content=response)


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    load_dotenv()
    # Nothing to do here...


if __name__ == "__main__":
    main()
