#!/usr/bin/python3
"""
A function that returns the number
of subscribers for a given subreddit
"""

from requests import get

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=headers)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
