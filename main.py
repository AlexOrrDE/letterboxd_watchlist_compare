import requests
import time
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (watchlist-overlap project)"}


def scrape_page(username, page):
    url = f"https://letterboxd.com/{username}/watchlist/page/{page}/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise ValueError(
            f"Got status {response.status_code} for {username} page {page}."
        )

    soup = BeautifulSoup(response.text, "html.parser")

    posters = soup.find_all(attrs={"data-item-slug": True})

    films = []
    for poster in posters:
        film = {
            "slug": poster["data-item-slug"],
            "name": poster["data-item-name"],
            "link": poster["data-item-link"],
        }
        films.append(film)

    time.sleep(0.1)
    return films


def scrape_watchlist(username):
    all_films = []
    page = 1
    while True:
        films = scrape_page(username, page)
        if not films:
            break
        all_films.extend(films)
        page += 1
    return all_films


def common_films_from_watchlists(watchlists):
    sets_of_slugs = [{film["slug"] for film in films} for films in watchlists.values()]
    common_slugs = set.intersection(*sets_of_slugs)

    lookup = {}
    for films in watchlists.values():
        for film in films:
            lookup[film["slug"]] = film

    return [lookup[slug] for slug in common_slugs]


def find_common_films(usernames):
    watchlists = {u: scrape_watchlist(u) for u in usernames}
    return common_films_from_watchlists(watchlists)
