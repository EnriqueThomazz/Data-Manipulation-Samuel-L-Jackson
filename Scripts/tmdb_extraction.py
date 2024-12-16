import requests
import json

# Url to get all movies and tv shows with Samuel L. Jackson (actor id 2231)
url = "https://api.themoviedb.org/3/person/2231?append_to_response=movie_credits,tv_credits"

access_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNmYzNWQxZDNiODBmYzIwYjg1ZGQzOTNiYWY5YjAzZSIsIm5iZiI6MTczMjg5MjU1MC41OTUxMzE2LCJzdWIiOiI2NjE2ZDdjYjg3M2YwMDAxNjQ5MThjMWMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ordX_S_tGl62QfY9af_p7j1qub5su8qMg_PKbdduhos"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_key}"
}

response = requests.get(url, headers=headers)

# Converting to a dict format
res = json.loads(response.text)

# Taking the movies from the response, splitting them into cast and crew
movies_cast = res["movie_credits"]["cast"]
movies_crew = res["movie_credits"]["crew"]

# Taking the series from the response, splitting them into cast and crew
series_cast = res["tv_credits"]["cast"]
series_crew = res["tv_credits"]["crew"]

# Saving the movies
with open("./Bronze/samuel_movies_cast.json", "w") as output:
        json.dump(movies_cast, output)

with open("./Bronze/samuel_movies_crew.json", "w") as output:
        json.dump(movies_crew, output)

# Saving the series
with open("./Bronze/samuel_series_cast.json", "w") as output:
        json.dump(series_cast, output)

with open("./Bronze/samuel_series_crew.json", "w") as output:
        json.dump(series_crew, output)
