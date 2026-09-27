import requests
import json

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3"

def search_team(team_name):
    """Search for a team and return its ID and info."""
    url = f"{BASE_URL}/searchteams.php"
    params = {"t": team_name}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Explore the response structure first
result = search_team("Girona")
print(json.dumps(result, indent=2))