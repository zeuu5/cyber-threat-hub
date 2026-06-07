import json
from datetime import datetime

with open("data/cves.json") as file:
    cves = json.load(file)

readme = f"# Cyber Threat Hub\n\n"
readme += f"Last Updated: {datetime.utcnow()} UTC\n\n"

readme += "## Latest CVEs\n\n"

for cve in cves:
    readme += f"- **{cve['id']}** : {cve['summary']}\n"

readme += "\n---\n"
readme += "\nAutomated threat intelligence updates.\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("README updated")