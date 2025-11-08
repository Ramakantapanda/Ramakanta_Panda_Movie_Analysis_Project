from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/movies")
def get_movies():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, title, year FROM movies LIMIT 50")
    movies = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(movies)

@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, title, year FROM movies WHERE movie_id = ?", (movie_id,))
    movie = cursor.fetchone()
    conn.close()
    return jsonify(dict(movie) if movie else {"error": "Movie not found"})

if __name__ == "__main__":
    app.run(debug=True)
