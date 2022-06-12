import re
from typing import List
from typing import NamedTuple

from bs4 import BeautifulSoup
import requests

LIST_URL = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"
PARK_URL_PATTERN = re.compile(r"https?://(www\.)?nps.gov/([a-z]{4})/?")

class Park(NamedTuple):
    name: str
    code: str
    state: str 
    longitude: float 
    latitude: float
    wikipedia_url: str 
    official_url: str
    established_date: str 
    visitation_2021: int 

    def as_csv_line(self) -> str:
        return (
            f'"{self.name}",'
            f'"{self.code}",'
            f'"{self.state}",'
            f'"{self.latitude}",'
            f'"{self.longitude}",'
            f'"{self.established_date}",'
            f'"{self.visitation_2021}",'
            f'"{self.wikipedia_url}",'
            f'"{self.official_url}"'
        )

def get_wikipedia_parks_table():
    wikipedia_list_page = requests.get(LIST_URL).text
    soup = BeautifulSoup(wikipedia_list_page, 'html.parser')
    return soup.find_all("table", class_="wikitable")[0].tbody

def get_official_url_from_wikipedia_url(wikipedia_url: str) -> str:
    wikipedia_detail_page = requests.get(wikipedia_url).text
    soup = BeautifulSoup(wikipedia_detail_page, 'html.parser')
    infobox = soup.find_all("table", class_="infobox")[0]
    for link in infobox.find_all("a"):
        if link["href"].startswith("https://www.nps.gov") or link["href"].startswith("https://nps.gov"):
            url = link["href"]
            if url.endswith("index.htm"):
                return url[:-9]
            return url

def get_park_object_from_wikipedia_table_row(wikipedia_row) -> Park:
        tds = wikipedia_row.find_all(["td", "th"])

        name = tds[0].a.string
        wikipedia_url = f"https://en.wikipedia.org{tds[0].a['href']}"
        state = tds[2].a.string
        latitude, longitude = list(map(float, tds[2].find_all("span", class_="geo")[0].string.split(";")))
        established = tds[3].span.string.replace(",", "")
        visitors = tds[5].string.replace(",", "").strip()

        official_url = get_official_url_from_wikipedia_url(wikipedia_url)
        park_code = PARK_URL_PATTERN.match(official_url).group(2)

        return Park(
            name=name, 
            code=park_code,
            state=state, 
            longitude=longitude, 
            latitude=latitude, 
            wikipedia_url=wikipedia_url,
            established_date=established, 
            visitation_2021=visitors,
            official_url=official_url,
        )

def parse_parks_list(wikipedia_table) -> List[Park]:
    table_rows = wikipedia_table.find_all("tr")[1:]  # strip away header row
    return [
        get_park_object_from_wikipedia_table_row(table_row) for table_row in table_rows
    ]

if __name__ == "__main__":
    # beautiful soup object of the <tbody> of the parks table from wikipedia
    wikipedia_parks_table = get_wikipedia_parks_table()
    # list of Park objects
    parks_list = parse_parks_list(wikipedia_parks_table)
    # print csv
    for park in parks_list:
        print(park.as_csv_line())
