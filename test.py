import requests
import pandas as pd

# Fetch launches data
launches_response = requests.get("https://api.spacexdata.com/v4/launches")
launches_data = launches_response.json()

# Extract rocket IDs
rocket_ids = list({launch.get('rocket') for launch in launches_data})

# Fetch rockets data
rockets_response = requests.post("https://api.spacexdata.com/v4/rockets/query", json={
    "query": {"_id": {"$in": rocket_ids}},
    "options": {"pagination": False}
})
rockets_data = rockets_response.json()['docs']
rocket_id_to_name = {rocket['id']: rocket['name'] for rocket in rockets_data}

# Prepare data for DataFrame
launch_ids = []
launch_names = []
launch_dates = []
rocket_names = []

for launch in launches_data:
    launch_ids.append(launch.get('id'))
    launch_names.append(launch.get('name', 'Unknown'))
    launch_dates.append(launch.get('date_utc', 'N/A'))
    rocket_id = launch.get('rocket')
    rocket_names.append(rocket_id_to_name.get(rocket_id, 'Unknown'))

# Create DataFrame
df = pd.DataFrame({
    'id': launch_ids,
    'name': launch_names,
    'date_utc': launch_dates,
    'rocket': rocket_names
})

print(df.head())