import requests
import json

url = "https://cve.circl.lu/api/last"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    latest_cves = []

    for item in data[:10]:
        latest_cves.append({
            "id": item.get("cve", "Unknown CVE"),
            "summary": item.get("summary", "No summary available")
        })

    with open("data/cves.json", "w") as file:
        json.dump(latest_cves, file, indent=4)

    print("CVE feed updated")

else:
    print("Failed to fetch CVEs")