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
 15.1️⃣ Correctness — “Does the pipeline work as expected?”

What you should say:

“My ETL pipeline works end-to-end.
It reads the input movie list, sends requests to the OMDb API, enriches the data with fields like Director, Genre, IMDb Rating, and Box Office, and finally generates an enriched CSV and loads it into SQLite for analysis.”

Proof points:

movies.csv → omdb_enrich.py → movies_enriched.csv → SQLite

SQL queries run successfully

The pipeline handles missing data and invalid API responses

2️⃣ Code Quality — “Is the code clean, readable, and well-organized?”

What you should say:

“I followed clean coding practices — modular functions, proper variable names, comments, and error handling.
The code is structured into logical parts: ETL script, schema file, and queries file.”

What makes your code good:

Separation of concerns

Helpful comments

Error handling with try/except

A requirements.txt file

Functions instead of writing all logic in main

3️⃣ Data Modeling — “Is the database schema logical and efficient?”

What you should say:

“I designed a simple but scalable schema.
The movies_enriched table stores key fields from OMDb.
If extended, I can normalize genres and create relationships using movie_genres.”

Why your design is good:

Avoids duplicate data

Easy to query

Can be scaled to many-to-many genre relationships

Supports analytics (ratings, box office, top directors, etc.)

4️⃣ Problem Solving — “How did you handle issues like missing data or API errors?”

What you should say:

“I added error handling to manage missing data and failed API calls.”

Examples:

If the API returns N/A, I substitute a default value.

If the movie is not found, I skip it but keep a log.

Added sleep() to avoid rate limiting.

Used try/except around requests.get() to avoid pipeline crashes.

5️⃣ Documentation — “Is the README.md clear and complete?”

What you should say:

“My README includes:

A project overview

Architecture diagram

Environment setup instructions

How to run the ETL

How to run SQL queries

Challenges and future improvements”

Why it matters:

Recruiters expect clarity and professionalism — your README achieves that.

6️⃣ Communication — “How clearly do you explain your decisions?”

What you should say:

“I explain the pipeline step-by-step, with reasoning behind each decision — why this data model, why SQLite, how error handling works, and how the solution can scale.”

Your strengths here:

You explain the flow clearly (Input → API → Transform → Database → Insights)

You show understanding of design choices

Confidently break down the architecture

## 16. Author

*Name:* Ramakanta Panda 
*Year:* 2024 
*Role:* Python Developer 
*phno:* 9668194892
*email:* ramakantapanda9668@gmail.com
*Branch:* Btech(csit)
