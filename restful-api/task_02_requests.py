import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        for line in response.json():
            print(line["title"])

def fetch_and_save_posts():
    response = requests.get(url)
    if response.status_code == 200:
        fieldnames = ["id", "body", "title"]
        with open("posts.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for line in response.json():
                writer.writerow({
                    'id': line['id'],
                    'body': line['body'],
                    'title': line['title']
                })
