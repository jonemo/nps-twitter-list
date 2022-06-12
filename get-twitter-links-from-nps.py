import csv
import json
from argparse import ArgumentParser
from pathlib import Path
from typing import Any
from typing import Iterator
from typing import List

import requests

def iter_infile_rows(infile: Path) -> Iterator[List[str]]:
    with infile.open("r", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            yield row

def normalize_url(url: Any) -> str:
    return str(url).replace("http://", "https://").replace("//www.", "//")

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('infile', type=Path, help='input csv file')
    parser.add_argument('outfile', type=Path, help='output csv file')
    args = parser.parse_args()

    new_csv_rows = []

    for row in iter_infile_rows(args.infile):
        park_code = row[1]        
        data_url = f"https://www.nps.gov/{park_code}/structured_data_{park_code}.json"
        decoded_data = requests.get(data_url).text.encode().decode('utf-8-sig')
        park_data = json.loads(decoded_data)

        twitter_url = normalize_url(park_data.get("twitterURL"))
        facebook_url = normalize_url(park_data.get("facebookURL"))
        youtube_url = normalize_url(park_data.get("youtubeURL"))
        flickr_url = normalize_url(park_data.get("flickrURL"))
        instagram_url = normalize_url(park_data.get("instagramURL"))

        new_csv_rows.append([
            *row, 
            twitter_url,
            facebook_url,
            youtube_url,
            flickr_url,
            instagram_url
        ])
        
    with args.outfile.open("w", newline='') as outfile:
        spamwriter = csv.writer(outfile, delimiter=',')
        spamwriter.writerows(new_csv_rows)
