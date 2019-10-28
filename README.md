# Autocomplete Search API

This Project demonstrates creating a website where an user can search for a movie name and see information like movie name, rating and cast for the same.

# Backend Developement:
## Scraping IMDB Website:

How to Scrape IMDB website for Names, Rating and cast of atleast 1000 movies:

Just have a look,
<a href="https://github.com/Saipriyagoka/Autocomplete-Search-API/blob/master/Scraping_IMDB.ipynb">Scraping_IMDB.ipynb</a>

## Backend Creation:
Created a Backend using Django with following API.
  1) GET: /autocomplete    
  
          given a search input prefix, display movie names that start with prefix,sorted by rating.        
          
          Example:      
            
            prefix = avg      
            
            Response ::        
              
              1. avengers        
              2. avengers endgame        
              ...
  2) GET: /movies/<movie_id>    
        
          given a movie_id return details of the movie like, name, cast and rating

# Getting Started
Here you go,
![Screenshot (38)](https://user-images.githubusercontent.com/49297116/67646774-a5296280-f955-11e9-941f-eee09769d519.png)
Autocomple search box,
![Screenshot (39)](https://user-images.githubusercontent.com/49297116/67646811-c8541200-f955-11e9-9a5c-cbb999500508.png)
Results,
![Screenshot (40)](https://user-images.githubusercontent.com/49297116/67646840-e883d100-f955-11e9-8e1f-82a5bd2a8397.png)
