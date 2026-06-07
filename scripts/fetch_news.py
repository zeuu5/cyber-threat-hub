import requests
import json

rss_url = "https://feeds.feedburner.com/TheHackersNews"

response = requests.get(rss_url)

with open("data/news.xml", "w", encoding="utf-8") as file:
    file.write(response.text)

print("News feed updated")