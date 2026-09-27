import requests
import json

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3"
GIRONA_TEAM_ID = "134700"
LALIGA2_LEAGUE_ID = "4400"

def get_last_results(team_id, league_id, num_results=5):
    """Fetch the last N results for a team, filtered by a specific league."""
    url = f"{BASE_URL}/eventslast.php"
    params = {"id": team_id}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    data = response.json()
    all_events = data.get("results", [])

    print(f"Raw events received: {len(all_events)}")
    for event in all_events:
        print(event.get("strEvent"), "-", event.get("idLeague"), "-", event.get("dateEvent"))

    # Filter to only include matches from the target league
    filtered_events = [
        event for event in all_events
        if event.get("idLeague") == league_id
    ]

    return filtered_events[:num_results]

# Test the filtered results
results = get_last_results(GIRONA_TEAM_ID, LALIGA2_LEAGUE_ID)
print(json.dumps(results, indent=2))