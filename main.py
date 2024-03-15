import requests
import os

api_key = os.getenv("PY_API_NEWS_KEY")
url = "https://newsapi.org/v2/everything?q=apple&from=2024-03-14&to=2024-03-14&sortBy=popularity&" \
       "apiKey=" + api_key

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])































