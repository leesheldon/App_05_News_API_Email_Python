import requests
import os
from send_email import send_email

api_key = os.getenv("Python_API_NEWS_KEY")

if api_key is None:
    print("API key is empty!")
    exit()

topic = "apple"
language = "en"
number_of_articles = 20

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-03-14&to=2024-03-14&" \
      "sortBy=popularity&" \
      f"pageSize={number_of_articles}&" \
      f"language={language}&" \
      "apiKey=" + api_key

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" + "\n"
title = ""
description = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"]

    if title is None or description is None:
        continue

    body = body + title + "\n" + description + "\n" + article["url"] + 2 * "\n"

# Convert content to UTF-8 format
body = body.encode("utf-8")

# Send the articles by email
send_email(message=body)
