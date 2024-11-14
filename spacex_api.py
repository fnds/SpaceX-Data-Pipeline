import requests
import pandas as pd

# Fetch launches data
launches_response = requests.get("https://api.spacexdata.com/v4/launches")
launches_data = launches_response.json()

# Prepare data for DataFrame
launch_ids = []
launch_names = []
launch_dates = []
rocket_names = []

for launch in launches_data:
    launch_ids.append(launch.get('id'))
    launch_names.append(launch.get('name', 'Unknown'))
    launch_dates.append(launch.get('date_utc', 'N/A'))

# Create DataFrame
df = pd.DataFrame({
    'id': launch_ids,
    'name': launch_names,
    'date_utc': launch_dates,
})

print(df.head())