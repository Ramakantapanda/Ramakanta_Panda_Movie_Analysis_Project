# Movie Data Enrichment and Analysis Project

This project enriches a movie dataset using the OMDb API and performs analytical SQL queries to understand trends in movie ratings, genres, directors, and box office performance.

---

## 1. Project Overview

We start with a base dataset of movie titles (movies.csv).  
Using an ETL (Extract, Transform, Load) script written in Python, we fetch additional movie metadata from the OMDb API such as:
This project performs movie data enrichment using the OMDb (Open Movie Database) API and then analyzes the enriched dataset using SQL.  
We start with a basic list of movie titles (movies.csv) and automatically fetch additional movie details such as:


- IMDb Rating
- Genre
- Director
- Release Year
- Plot Summary
- Box Office Collection

The final enriched output is stored in movies_enriched.csv, which is then loaded into SQLite for analytical querying.

This project demonstrates:
- ETL (Extract, Transform, Load) workflow in Python
- API data consumption
- Data cleaning and transformation
- SQL-based data analytics

## 2. Project Structure

Movie_project/
│
├── movies.csv # Input dataset 
├── omdb_enrich.py # Python ETL script
├── movies_enriched.csv # Output enriched dataset 
├── queries.sql # SQL analysis queries
├── README.md # Project documentation
└── movies.db # SQLite database 

---

## 3. Environment Setup

### *Step 1: Install Python (if not installed)*  
Download from: https://www.python.org/downloads/

### *Step 2: Install Required Libraries*


### **Step 3: Place your OMDb API Key in .env**
Create a new file named .env (same folder) and add:

---

## 4. Running the ETL (Data Enrichment Script)

Run this command inside the project directory:


---

This will:
- Read movies.csv
- Fetch details from OMDb API
- Save results in movies_enriched.csv

If the file appears, enrichment is successful.

---

## 5. Loading Data into SQLite for Analysis


Verify import:


---

## 6. Running Analytical Queries

To run all queries:

Example query included:
- Highest rated movie
- Top directors by average ratings
- Genre frequency & popularity
- Box office ranking
- Movie release trends per year

---

## 7. Design Choices & Assumptions

| Design Decision | Reason |
|-----------------|--------|
| OMDb API was chosen | Public, easy-to-query movie metadata API |
| Data stored in CSV | Allows easy debugging and portability |
| SQLite for analytics | Lightweight and requires no server setup |
| Delay (0.2 sec) in API calls | Prevents API rate-limit blocking |

*Assumption:* Movie titles in movies.csv are reasonably spelled.  
If a title is inaccurate, the API may return Movie not found.

---

## 8. Challenges & How I Solved

| Challenge | Solution |
|----------|----------|
| API returning Movie not found for some titles | Implemented check to skip missing movies |
| Inconsistent formatting of BoxOffice values | Cleaned values by removing $ and , before casting |
| Some movies returning N/A values | Handled null values in SQL and during DataFrame creation |
| Running SQL queries on Windows | Used SQLite CLI instead of requiring MySQL/PostgreSQL |

These improvements ensured data consistency and stable analysis results.

---




## 9. Dataset Used

| File | Description |
|------|-------------|
| movies.csv | Original dataset containing movie names |
| movies_enriched.csv | Final dataset enriched with API data |

---

## 10. Tools & Technologies

- Python
- OMDb API
- SQLite Database
- SQL for Data Analysis

---

## 11. ETL Process (Python Script)

1. Read movie titles from movies.csv.
2. For each title, send request to OMDb API:




3. Extract required fields from JSON response.
4. Append to dataset.
5. Save final output as movies_enriched.csv.

---

## 12. Loading Data Into SQLite

To load the enriched dataset into SQLite:


Verify:


---

## 13. Project Insights (Based on Results)

| Analysis | Insight |
|---------|---------|
| Highest Rated Movie | Returned the movie with the highest IMDb rating |
| Top Directors | Ranked directors with at least 3 movies |
| Box Office Ranking | Identified highest-grossing movies |
| Popular Genre Types | Listed genres appearing most frequently |
| Rating by Genre | Showed how genre influences ratings |
| Release Trends | Displayed how movie counts vary over years |

(Your actual output will depend on your dataset.)

---

## 14. How to Run the Project Yourself

1. Download project folder.
2. Install Python:
3. Run ETL:
4.  Load movies_enriched.csv into SQLite (commands above).
5. Execute analysis:


---

## 15. Author

*Name:* Ramakanta Panda 
*Year:* 2024 
*Role:* Python Developer 
*phno:* 9668194892
*email:* ramakantapanda9668@gmail.com
*Branch:* Btech(csit)
