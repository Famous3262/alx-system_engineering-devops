#!/usr/bin/python3
"""
A function that returns the number
of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    response = get(url, headers=user_agent)
    results = response.json()

    if response.status_code == 404:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
