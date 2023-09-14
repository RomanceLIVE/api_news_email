import requests

api_key = "a693352cfdda4fe78f4cc555a67c4ba1"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-08-14&sortBy=publishedAt&apiKey" \
      "=a693352cfdda4fe78f4cc555a67c4ba1"
# we broke the string with \
# url = "https://finance.yahoo.com"

request_url = requests.get(url)
content = request_url.text
print(content)
