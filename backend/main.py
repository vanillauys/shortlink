# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas import Schemas
from dotenv import load_dotenv


# ---------------------------------------------------------------------------- #
# --- App Configuration ------------------------------------------------------ #
# ---------------------------------------------------------------------------- #

load_dotenv()
schemas = Schemas()

TAGS_METADATA = [
    {
        "name": "Testing",
        "description": "Routes to test functionality.",
        "externalDocs": {
            "description": "FastAPI Documentation",
            "url": "https://fastapi.tiangolo.com/",
        }
    }
]


# Configure the API with detailed description
app = FastAPI(
    title="Shortener Backend",
    description="URL Shortener with cutt.ly",
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "Wihan Uys",
        "url": "https://vanillauys.vercel.app/about",
        "email": "wihan@duck.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://spdx.org/licenses/MIT.html",
    },
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
        'detail': "https://vanillauys-1-t9282601.deta.app/"
    }
    return JSONResponse(status_code=200, content=response)


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    load_dotenv()
    # Nothing to do here...


if __name__ == "__main__":
    main()
