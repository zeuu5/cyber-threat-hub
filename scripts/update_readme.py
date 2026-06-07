import json
from datetime import datetime
import xml.etree.ElementTree as ET

# Load CVEs
with open("data/cves.json") as file:
    cves = json.load(file)

# Parse news XML
tree = ET.parse("data/news.xml")
root = tree.getroot()

items = root.findall(".//item")

readme = "# Cyber Threat Hub\n\n"
readme += f"Last Updated: {datetime.now().astimezone()} UTC\n\n"

# CVE Section
readme += "## Latest CVEs\n\n"

for cve in cves:
    readme += f"- **{cve['id']}** : {cve['summary']}\n"

# News Section
readme += "\n## Latest Cybersecurity News\n\n"

for item in items[:5]:
    title = item.find("title").text
    link = item.find("link").text

    readme += f"- [{title}]({link})\n"

readme += "\n---\n"
readme += "\nAutomated threat intelligence updates.\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("README updated")