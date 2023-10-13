#!/usr/bin/python3

"""
prints the first 10 hot posts listed 
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'hello_API/0.0.1'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        data = results.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
