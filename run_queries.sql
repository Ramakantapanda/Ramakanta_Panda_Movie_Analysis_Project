
.headers on
.mode csv
.import movies_enriched.csv movies_enriched

.output highest_imdb.csv
SELECT Title, Director, imdbRating
FROM movies_enriched
WHERE imdbRating IS NOT NULL
ORDER BY CAST(imdbRating AS FLOAT) DESC
LIMIT 1;
.output stdout

.output top_directors.csv
SELECT Director, AVG(CAST(imdbRating AS FLOAT)) AS avg_rating, COUNT(*) AS movie_count
FROM movies_enriched
WHERE imdbRating IS NOT NULL AND Director IS NOT NULL
GROUP BY Director
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC
LIMIT 5;
.output stdout

.output top_boxoffice.csv
SELECT Title, Director, BoxOffice
FROM movies_enriched
WHERE BoxOffice IS NOT NULL
ORDER BY CAST(REPLACE(REPLACE(BoxOffice, '$', ''), ',', '') AS BIGINT) DESC
LIMIT 10;
.output stdout

.output top_genres.csv
SELECT Genre, COUNT(*) AS movie_count
FROM movies_enriched
WHERE Genre IS NOT NULL
GROUP BY Genre
ORDER BY movie_count DESC
LIMIT 10;
.output stdout

.output avg_rating_genre.csv
SELECT Genre, AVG(CAST(imdbRating AS FLOAT)) AS avg_rating
FROM movies_enriched
WHERE imdbRating IS NOT NULL AND Genre IS NOT NULL
GROUP BY Genre
ORDER BY avg_rating DESC
LIMIT 10;
.output stdout

.output movies_per_year.csv
SELECT SUBSTR(Released, -4) AS Year, COUNT(*) AS movie_count
FROM movies_enriched
WHERE Released IS NOT NULL
GROUP BY Year
ORDER BY Year;
.output stdout

.exit
