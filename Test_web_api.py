import requests
from send_email import send_email

topic = "tesla"
# tesla was hardcoded into the url
# we replaced it with the variable inside the url

api_key = "a693352cfdda4fe78f4cc555a67c4ba1"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-08-14&sortBy=publishedAt&apiKey" \
      "=a693352cfdda4fe78f4cc555a67c4ba1&language=en"
# added &language=en at end of url to display only english pages
# we broke the string with \
# url = "https://finance.yahoo.com"

#Make request
request_url = requests.get(url)


# content = request_url.text
#Get data in dictionary format
content = request_url.json()
# json because we need a dictionary format
# Access the article titles and description

body = "Subject: Today's news" + "\n"
for article in content["articles"]:

      if article["title"] is not None:
            body += article["title"] + "\n"
      if article["description"] is not None:
            body += article["description"] + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
