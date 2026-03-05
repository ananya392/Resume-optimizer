import requests
import os

API_KEY = os.getenv("SEARCHAPI_API_KEY")

def search_role_skills(role):
    url = "https://www.searchapi.io/api/v1/search"

    params = {
        "engine": "google",
        "q": f"skills required for {role}",
        "api_key":API_KEY
    }
    response = requests.get(url, params=params)
    data=response.json()

    snippets = []

    for result in data.get("organic_results", []):
        if "snippet" in result:
            snippets.append(result["snippet"])

    return " ".join(snippets)