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
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = ""
title = ""
description = ""
image_link = ""
article_url = ""

for article in content["articles"]:
    title = article["title"]
    description = article["description"]
    article_url = article["url"]
    image_link = article['urlToImage']

    if title is None or description is None or article_url is None or image_link is None:
        continue

    image_html = f"<img src='{image_link}' alt='image' width=380 height=300 />"

    # body = body + title + "\n" + description + "\n" + article_url + "\n" + image_html + 2 * "\n"

    body += f"<h1>{title}</h1>\n<p>{description}</p>\n<p><a href='{article_url}'>{article_url}</a></p>" \
            f"\n{image_html}\n\n"

# Send the articles by email
send_email(message=body)
