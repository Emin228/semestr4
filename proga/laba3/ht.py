from urllib.parse import parse_qs

from fastapi import params
import httpx

URL = "https://www.cbr.ru/scripts/XML_daily.asp"

async def fetch_curr():
    try:    
        async with httpx.AsyncClient() as client:
            response = await client.get(URL)
            response.raise_for_status()
            return response.text
    
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        return None

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return None




