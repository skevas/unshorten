[![Requirements Status](https://requires.io/github/skevas/unshorten/requirements.svg?branch=master)](https://requires.io/github/skevas/unshorten/requirements/?branch=master)

## Synopsis

A simple tool to check if a given URL is a shortened URL (e.g., from bit.ly). You could either check if the given URL starts with a known URL shortening service or you could use the unshortener. The later one connects to the given URL and returns the original URL (when the server returns with a HTTP 200) or the URL of the redirect (when the server return a HTTP 300-308). You will not connect to the redirect if there is any.

***This code hasn't been tested in any production system!*** It works as expected for a very limited testset I tried. You have been warned!

## Code Example

```
from isurlunshorten import *
Unshortener.unshorten_url('http://bit.ly/1ixYuRi')
IsUrlShortener.is_url_shortener('http://bit.ly/1ixYuRi')
```

## Motivation

I spend some of my free time with a toy project where I needed a way to detect URLs from shorteners. 

## Installation

Clone this repository and run:
```
sudo python3 setup.py install
```

## Tests

```
nose2 --with-coverage
```

## License

MIT