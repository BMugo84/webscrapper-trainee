
import json

har_file = "C:/Users/BM/scrapper/har_reader/har_file.har" # replace with the name of your HAR file

with open(har_file, "r") as f:
    har_data = json.load(f)

entries = har_data["log"]["entries"]
total_size = 0

for entry in entries:
    response = entry["response"]
    content = response.get("content", {})
    size = content.get("size", 0)
    total_size += size

print(f"Total size: {round(total_size/1000000, 2)} Megabytes")