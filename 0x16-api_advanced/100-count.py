#!/usr/bin/python3
"""A recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords"""

import requests


def count_words(subreddit, word_list):
    """parses the title of all hot articles and prints a sorted count"""
    r = requests.get(r'https://www.reddit.com/r/{}/hot/.json'
                     .format(subreddit), headers={'User-agent': 'x'},
                     allow_redirects=False)
    l = r.json().get('data').get('children')
    if r.status_code != 200:
        return None
