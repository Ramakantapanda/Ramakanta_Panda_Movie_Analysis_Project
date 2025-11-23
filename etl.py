import pandas as pd
import requests
import sqlite3
import time

API_KEY = "your_omdb_api_key_here"     # ← Replace with your actual key
INPUT_CSV = "movies.csv"
OUTPUT_CSV = "movies_enriched.csv"
DB_NAME = "movies.db"


def fetch_from_omdb(title):
    """Fetch movie details from OMDb API with error handling."""
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        # If movie not found
        if data.get("Response") == "False":
            return {
                "Director": None,
                "Genre": None,
                "imdbRating": None,
                "BoxOffice": None,
                "Released": None,
            }

        return {
            "Director": data.get("Director"),
            "Genre": data.get("Genre"),
            "imdbRating": data.get("imdbRating"),
            "BoxOffice": data.get("BoxOffice"),
            "Released": data.get("Released"),
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "Director": None,
            "Genre": None,
            "imdbRating": None,
            "BoxOffice": None,
            "Released": None,
        }


def enrich_movies():
    """Reads movies.csv, fetches OMDb data, and writes enriched CSV."""
    df = pd.read_csv(INPUT_CSV)
    enriched_data = []

    print("Starting OMDb enrichment...")

    for index, row in df.iterrows():
        title = row["title"]
        print(f"Fetching: {title}")

        movie_data = fetch_from_omdb(title)
        enriched_data.append(movie_data)

        time.sleep(1)  # Prevent API rate limit issues

    enriched_df = pd.concat([df, pd.DataFrame(enriched_data)], axis=1)
    enriched_df.to_csv(OUTPUT_CSV, index=False)

    print("Enrichment completed. Saved to movies_enriched.csv")


def load_to_sqlite():
    """Loads enriched CSV into SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_csv(OUTPUT_CSV)

    df.to_sql("movies_enriched", conn, if_exists="replace", index=False)

    print("Data successfully loaded into movies.db (SQLite)")
    conn.close()


if __name__ == "__main__":
    print("===== ETL Pipeline Started =====")

    enrich_movies()
    load_to_sqlite()

    print("===== ETL Pipeline Completed Successfully =====")
