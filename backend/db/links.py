# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
from deta import Deta
from dotenv import load_dotenv
from schemas import Schemas
from typing import Tuple


# ---------------------------------------------------------------------------- #
# --- Links Database --------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


load_dotenv()

class LinksDB():

    schemas = Schemas()
    PROJECT_KEY = os.getenv('DETA_PROJECT_KEY')
    deta = Deta(PROJECT_KEY)
    links = deta.Base('shrtn')


    def create_link(self, link: schemas.Link) -> Tuple[int, str]:
        data = {
            'shortLink': link.shortLink,
            'fullLink': link.fullLink,
            'date': link.date,
            'title': link.title,
        }
        try:
            self.links.put(data)
            return 200, f"Successfully created shortlink for '{link.fullLink}'."
        except Exception:
            return 500, f"An error occured while saving shortlink for '{link.fullLink}'"

