import requests
query = input("What do you want to search for? ")
api = "0bca5b1f3b7d4ddda7e413b89f1bcceb"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-24&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n*****************\n")