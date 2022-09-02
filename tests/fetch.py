import requests

req_url = "https://newsapi.org/v2/everything?q=tesla&from=2022-07-30&sortBy=publishedAt&apiKey=cd6f44f57521402dab39db73fde51eb4"

output_url = requests.get(req_url)
print(output_url.json())
print(output_url.status_code)