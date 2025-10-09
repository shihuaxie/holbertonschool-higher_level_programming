#!/usr/bin/python3
"""This module fetches posts from JSONPlaceholder using requests."""
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status code + each title."""
    res = requests.get(URL)
    print("Status Code:", res.status_code)

    if res.status_code == 200:
        posts = res.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save them into posts.csv with id, title, body."""
    res = requests.get(URL)

    if res.status_code == 200:
        posts = res.json()

    # Get id, title, and body
    data_rows = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

    # write above data to csv file names posts.csv
    fieldnames = ["id", "title", "body"]

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # write table header first
        writer.writerow(fieldnames)
        # write content corresponding to header
        for data_row in data_rows:
            writer.writerow(
                [data_row["id"], data_row["title"], data_row["body"]]
            )
