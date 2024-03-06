#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    r = requests.get(r'https://www.reddit.com/r/{}/hot/.json'
                     .format(subreddit), headers={'User-agent': 'x'},
                     allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    l = r.json().get('data').get('children')
    for data in l[:10]:
        da = data['data']
        title = da.get('title')
        print(title)
