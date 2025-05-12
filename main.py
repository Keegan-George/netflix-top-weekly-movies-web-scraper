"""
A web scraper that captures Netflix's top 10 most viewed movies globally for the current week and writes them to a text file.
"""

import requests
from bs4 import BeautifulSoup

NETFLIX_URL = "https://www.netflix.com/tudum/top10"

response = requests.get(NETFLIX_URL).text
soup = BeautifulSoup(response, "lxml")

# html table containing the list of movies
current_top_movies = soup.select("tbody tr")

# template to maintain column widths
TEMPLATE = "{0:<6}|{1:<30}|{2:<7}|{3:<15}|{4:<9}|{5}\n"

with open("netflix-current-top-10.txt", "w") as netflix_file:
    # write column headers
    netflix_file.write(
        TEMPLATE.format("Rank", "Title", "Weeks", "Views", "Runtime", "Hours Viewed")
    )

    # capture movie details from each row
    for row in current_top_movies:
        rank_title, weeks, views, runtime, hours_viewed = [
            column.text for column in row.find_all("td")
        ]

        # split the rank and column into their own strings
        rank, title = rank_title[:2], rank_title[2:]

        # write movie details
        netflix_file.write(
            TEMPLATE.format(rank, title, weeks, views, runtime, hours_viewed)
        )
