SELECT title, rating FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE year = 2010 AND rating not NULL ORDER BY rating DESC, title;
