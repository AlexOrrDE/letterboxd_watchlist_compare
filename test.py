from main import common_films_from_watchlists

watchlist_a = [
    {"slug": "shared_movie", "name": "Shared", "link": "/film/shared-movie/"},
    {"slug": "semi_shared", "name": "Semi Shared", "link": "/film/semi-shared/"},
    {"slug": "unique_1", "name": "Unique 1", "link": "/film/unique-1/"}
]

watchlist_b = [
    {"slug": "semi_shared", "name": "Semi Shared Movie", "link": "/film/semi-shared/"},
    {"slug": "shared_movie", "name": "Shared", "link": "/film/shared-movie/"},
    {"slug": "unique_2", "name": "Unique 2", "link": "/film/unique-2/"}
]

watchlist_c = [
    {"slug": "unique_3", "name": "Unique 3", "link": "/film/unique-3/"},
    {"slug": "unique_4", "name": "Unique 4", "link": "/film/unique-4/"},
    {"slug": "shared_movie", "name": "Shared Movie", "link": "/film/shared-movie/"}
]

watchlists = {"a": watchlist_a, "b": watchlist_b, "c": watchlist_c}
result = common_films_from_watchlists(watchlists)
result_slugs = {film["slug"] for film in result}

print(result)
assert result_slugs == {"shared_movie"}, f"got {result_slugs}"
assert "semi_shared" not in result_slugs, f"semi_shared leaked in: {result_slugs}"
print("passed")