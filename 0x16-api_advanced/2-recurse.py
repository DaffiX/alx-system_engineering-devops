#!/usr/bin/python3
"""A recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hotlist=[], after="", count=0):
    """all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hotlist.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hotlist, after, count)
    return hotlist
