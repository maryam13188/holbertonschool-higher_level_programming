-- 16-shows_by_genre.sql
-- Lists all shows and all genres linked to that show
-- If a show doesn't have a genre, display NULL
-- Results: tv_shows.title - tv_genres.name
-- Sorted by show title and genre name in ascending order

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
