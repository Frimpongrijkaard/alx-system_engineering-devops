#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
aft = None


def recurse(subreddit, hot_list=[]):
    """return the top ten post titles recursively"""
    global aft
    user_agent = {'User-Agent': 'api_advanced'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': aft}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        data = results.json().get("data").get("after")
        if data is not None:
            aft = data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
