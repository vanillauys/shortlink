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
            return 200, {'detail': f"Successfully created shortlink for '{link.fullLink}'."}
        except Exception:
            return 500, {'detail': f"An error occured while saving shortlink for '{link.fullLink}'"}


    def get_all(self) -> Tuple[int, list]:
        try:
            res = self.links.fetch()
            all_items = res.items

            # fetch until last is 'None'
            while res.last:
                res = self.links.fetch(last=res.last)
                all_items += res.items
            return 200, all_items
        except Exception:
            return 500, {'detail': "An error occured while fetching all shortlinks"}
    

    def delete_link(self, key: str) -> Tuple[int, str]:
        try:
            self.links.delete("one")
            return 200, {'detail': f"Successfully deleted {key}"}
        except Exception:
            return 500, {'detail': f"An error occured while deleting {key}"}

