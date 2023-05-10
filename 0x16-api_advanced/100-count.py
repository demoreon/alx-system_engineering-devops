#!/usr/bin/python3

""" reddit construct"""
import requests


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): A dictionary of word counts.
        after (str): The `after` parameter for the Reddit API.
        count (int): The number of posts processed so far.
    """
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("")
        return

    results = response.json()["data"]
    after = results.get("after")
    count += results.get("dist")

    for c in results["children"]:
        title = c["data"]["title"].lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if word in instances:
                    instances[word] += times
                else:
                    instances[word] = times

    if after is None:
        if not instances:
            print("")
            return
        instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
        for word, count in instances:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, instances, after, count)


