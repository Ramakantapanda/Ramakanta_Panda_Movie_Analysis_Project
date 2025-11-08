SELECT Title, Director, imdbRating
FROM movies_enriched
WHERE imdbRating IS NOT NULL
ORDER BY CAST(imdbRating AS FLOAT) DESC
LIMIT 1;

SELECT Director, AVG(CAST(imdbRating AS FLOAT)) AS avg_rating, COUNT(*) AS movie_count
FROM movies_enriched
WHERE imdbRating IS NOT NULL AND Director IS NOT NULL
GROUP BY Director
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC
LIMIT 5;

SELECT Title, Director, BoxOffice
FROM movies_enriched
WHERE BoxOffice IS NOT NULL
ORDER BY 
    CAST(REPLACE(REPLACE(BoxOffice, '$', ''), ',', '') AS BIGINT) DESC
LIMIT 10;

SELECT Genre, COUNT(*) AS movie_count
FROM movies_enriched
WHERE Genre IS NOT NULL
GROUP BY Genre
ORDER BY movie_count DESC
LIMIT 10;

SELECT Genre, AVG(CAST(imdbRating AS FLOAT)) AS avg_rating
FROM movies_enriched
WHERE imdbRating IS NOT NULL AND Genre IS NOT NULL
GROUP BY Genre
ORDER BY avg_rating DESC
LIMIT 10;

SELECT SUBSTR(Released, -4) AS Year, COUNT(*) AS movie_count
FROM movies_enriched
WHERE Released IS NOT NULL
GROUP BY Year
ORDER BY Year;
