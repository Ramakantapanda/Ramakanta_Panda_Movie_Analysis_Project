import requests
import pandas as pd


OMDB_API_KEY="e4506d45"

def fetch_movie_details(title):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}&plot=full"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True":
            return {
                "Title": data.get("Title"),
                "Director": data.get("Director"),
                "Plot": data.get("Plot"),
                "BoxOffice": data.get("BoxOffice"),
                "Genre": data.get("Genre"),
                "Released": data.get("Released"),
                "Runtime": data.get("Runtime"),
                "imdbRating": data.get("imdbRating"),
            }
        else:
            print(f"Movie not found: {title}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {title}: {e}")
    return {
        "Title": title,
        "Director": None,
        "Plot": None,
        "BoxOffice": None,
        "Genre": None,
        "Released": None,
        "Runtime": None,
        "imdbRating": None,
    }

movies_df = pd.read_csv("movies.csv")
enriched_movies = []

for i, title in enumerate(movies_df['title'], 1):
    details = fetch_movie_details(title)
    enriched_movies.append(details)
    print(f"{i}/{len(movies_df)}: Fetched {title}")

enriched_df = pd.DataFrame(enriched_movies)
enriched_df.to_csv("movies_enriched.csv", index=False)

print("Enrichment complete! Check movies_enriched.csv")
