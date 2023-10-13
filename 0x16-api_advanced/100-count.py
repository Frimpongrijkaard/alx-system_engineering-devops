#!/usr/bin/python3

""" a recursive function that queries the Reddit API"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """function that count all words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for subject in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(wordlists)):
                    if wordlists[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(wordlists)):
                for j in range(i + 1, len(wordlists)):
                    if wordlists[i].lower() == wordlists[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(wordlists)):
                for j in range(i, len(wordlists)):
                    if (count[j] > count[i] or
                            (wordlists[i] > wordlists[j] and
                             count[j] == count[i])):
                        mini = count[i]
                        count[i] = count[j]
                        count[j] = mini
                        mini = wordlists[i]
                        wordlists[i] = wordlists[j]
                        wordlists[j] = mini

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, wordlists, after, count)
