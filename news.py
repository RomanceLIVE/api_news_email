import requests

api_key = "a693352cfdda4fe78f4cc555a67c4ba1"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-08-14&sortBy=publishedAt&apiKey" \
      "=a693352cfdda4fe78f4cc555a67c4ba1"
# we broke the string with \
# url = "https://finance.yahoo.com"

#Make request
request_url = requests.get(url)


# content = request_url.text
#Get data in dictionary format
content = request_url.json()
# json because we need a dictionary format
# Access the article titles and description
for article in (content["articles"]):
      print(article["title"])
      print(article["description"])
