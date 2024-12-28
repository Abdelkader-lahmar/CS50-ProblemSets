SELECT name FROM people JOIN movies, ratings, directors ON ratings.movie_id = movies.id AND movies.id = directors.movie_id AND directors.person_id = people.id WHERE ratings.rating >= 9 GROUP BY name;
