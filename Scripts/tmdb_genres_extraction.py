import requests
import json

# URLs to get all genres on series and movies
url_series = "https://api.themoviedb.org/3/genre/tv/list"
url_movies = "https://api.themoviedb.org/3/genre/movie/list"

access_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNmYzNWQxZDNiODBmYzIwYjg1ZGQzOTNiYWY5YjAzZSIsIm5iZiI6MTczMjg5MjU1MC41OTUxMzE2LCJzdWIiOiI2NjE2ZDdjYjg3M2YwMDAxNjQ5MThjMWMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ordX_S_tGl62QfY9af_p7j1qub5su8qMg_PKbdduhos"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_key}"
}

response_series = requests.get(url_series, headers=headers)

response_movies = requests.get(url_movies, headers=headers)

# Converting to a dict format
res_series = json.loads(response_series.text)
res_movies = json.loads(response_movies.text)

# Saving the genres
with open("./Bronze/tmdb_genres.json", "w") as output:
        json.dump(res_movies["genres"] + res_series["genres"], output)