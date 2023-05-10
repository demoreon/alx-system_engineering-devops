#!/usr/bin/python3

"""A program that counts occurrences of words in the titles of Reddit posts."""

import requests


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """Counts the number of times each word in word_list occurs in the titles of
    the hot posts in the given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list of str): The words to search for.
        instances (dict): A dictionary containing the counts of each word.
        after (str): The 'after' parameter to use for the Reddit API.
        count (int): The total number of posts processed so far.

    Returns:
        A dictionary containing the counts of each word in word_list.
    """
    if instances is None:
        instances = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("")
        return {}

    results = response.json()["data"]
    after = results.get("after")
    count += results.get("dist")

    # Process each post recursively
    def process_post(post):
        title = post["data"]["title"].lower().split()

        def process_word(word):
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if word in instances:
                    instances[word] += times
                else:
                    instances[word] = times

        list(map(process_word, word_list))

    list(map(process_post, results["children"]))

    if after is None:
        if not instances:
            print("")
            return {}
        instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
        for word, count in instances:
            print("{}: {}".format(word, count))
        return instances
    else:
        return count_words(subreddit, word_list, instances, after, count)
