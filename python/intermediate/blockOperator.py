import requests

fetch_url = "https://newsapi.org/v2/everything?q=tesla&from=2022-09-25&sortBy=publishedAt&apiKey=391b845c95b64b0ea4a5c67fe7d31a41"

with open("../../generated/Jimmy.txt") as f:
    print(f.read())


with open("../../generated/api-data.txt", "wt", encoding="utf-8") as s:
    """ Add the new text from the existing content """
    fetch_url_data = requests.get(fetch_url)
    json_fetch_data = str(fetch_url_data.json())
    appends = s.write(json_fetch_data)

with open("../../generated/scratch.txt", "r") as read_file:
    print(read_file.read())



