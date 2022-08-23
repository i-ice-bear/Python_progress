import requests

fetch_url = "https://newsapi.org/v2/everything?q=tesla&from=2022-07-23&sortBy=publishedAt&apiKey" \
            "=cd6f44f57521402dab39db73fde51eb4 "
r = requests.get(fetch_url)
print(r.json())
print(r.status_code)
