# Movie Parsing Web Application

This project is a one-page web application designed to scrape movie data from a website, store it in a database, and display the movies on the main page in a table format. The user can load new movies from the website by clicking a button that triggers a backend request to scrape, process, and display the top 100 movies, sorted by IMDb rating.

## Features

- Scrapes movies from a website with all basic information (title, description, image, IMDb rating).
- Stores movie data in a SQL database using SQLAlchemy.
- Displays all parsed movies in a sortable table on the frontend.
- Allows users to load new movies by clicking a "Load Movies" button.
- Automatically displays previously scraped movies upon page load.
- Images are stored locally.

## Technologies Used

- **Backend**: FastAPI, SQLAlchemy
- **Frontend**: Bootstrap, jQuery
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Setup and Installation

To run the project using Docker and Docker Compose, follow these steps:

```bash
git clone https://github.com/your-username/movie-parsing-app.git
cd la_chatte
docker-compose up -d
```   
