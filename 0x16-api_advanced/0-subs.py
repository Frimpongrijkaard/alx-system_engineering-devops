#!/usr/bin/python3

""" this script perform extracting of number
    of subscribers.
"""
import requests

def number_of_subscribers(subreddit):
    """return the number of subscribers """

    headers = {"User-agent" : "myapp_API/0.0.1"}
    response = requests.get(f"https://oauth.reddit.com/r/{subreddit}/about.json", headers=headers)
    if response.status_code == 200:
        res = response.json()
        if 'data' in res['data'] and 'subscribers' in res['subscribers']:
            return res['data']['subscribers']
    else:
        return 0

