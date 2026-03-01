#!/usr/bin/python3
"""fetch from JSONPlaceholder"""


import requests
import csv

url = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_and_print_posts():
    """fetch and print"""
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for posts in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure required data
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)