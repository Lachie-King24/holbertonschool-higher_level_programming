-- 10-genre_id_by_show.sql
SELECT title, genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.tv_show_id
ORDER BY title, genre_id;