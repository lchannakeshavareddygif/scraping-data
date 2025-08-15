import requests
import pandas as pd

# RemoteOK API endpoint
url = "https://remoteok.com/api"

# Get the data from the API
response = requests.get(url)
data = response.json()

# Skip the metadata (first element in the JSON)
jobs = data[1:]

# Extract relevant fields
job_list = []
for job in jobs:
    job_list.append({
        "Company Name": job.get("company", ""),
        "Job Role": job.get("position", ""),
        "Location": job.get("location", ""),
        "Features/Tags": ", ".join(job.get("tags", []))
    })

# Create DataFrame
df = pd.DataFrame(job_list)

# Save to CSV
df.to_csv("remoteok_jobs.csv", index=False)
print("Data saved to remoteok_jobs.csv")
