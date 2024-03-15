import requests
import os
from send_email import send_email

api_key = os.getenv("Python_API_NEWS_KEY")

if api_key is None:
    print("API key is empty!")
    exit()

url = "https://newsapi.org/v2/everything?q=apple&from=2024-03-14&to=2024-03-14&sortBy=popularity&" \
       "apiKey=" + api_key

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
title = ""
description = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"]

    if title is None or description is None:
        continue

    body = body + title + "\n" + description + 2*"\n"

# Convert content to UTF-8 format
body = body.encode("utf-8")

# Send the articles by email
send_email(raw_message=body)






























