# nps-twitter-list

Scraping scripts for building a list of US National Park Twitter accounts.

This repo is **not maintained**.
The repo contents are a half-baked note-to-self, but you are welcome to use it under the terms of the included license.

## Usage 

```sh
python build-npslist-from-wikipedia.py > nps-twitter-1.csv
python get-twitter-links-from-nps.py nps-twitter-1.csv nps-twitter-2.csv
# edit twurlstats.py
python twurlstats.py
```

## Parks that have a twitter account but don't list it on their official website:

* https://twitter.com/CongareeNPS
* https://twitter.com/GreatDunesNPS
* https://twitter.com/VoyageursNPS
* https://twitter.com/WhiteSandNps
