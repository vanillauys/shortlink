# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
import json
import asyncio
import httpx
import urllib
from dotenv import load_dotenv


# ---------------------------------------------------------------------------- #
# --- Shortener Class -------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


load_dotenv()
class Shortener():


    key = os.getenv('CUTTLY_KEY')

    async def shorten_link(self, url):
        url = urllib.parse.quote(url)
        async with httpx.AsyncClient() as client:
            r = await client.get(f'https://cutt.ly/api/api.php?key={self.key}&short={url}')

        try:
            r = json.loads(r.text)['url']
            status = r['status']
        except Exception:
            status = None

        if status == 1:
            return 409, 'The url has already been shortened.'
        elif status == 2:
            return 400, 'The url you entered is not a valid link.'
        elif status == 3:
            return 409, 'The custom name is already taken.'
        elif status == 4:
            return 401, 'The API key is invalid.'
        elif status == 5:
            return 400, "The url you entered didn't pass the validation, check for illegal characters."
        elif status == 6:
            return 401, "The url you entered is from a blocked domain."
        elif status == 7:
            return 200, r
        elif status == 8:
            return 429, 'There were too many requests, please try again later.'
        else:
            return 500, 'Something went wrong.'


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


async def main():
    shortener = Shortener()
    code, a = await shortener.shorten_link('https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses')
    print(f"code: {code}")
    print(a)


if __name__ == "__main__":
    asyncio.run(main())
