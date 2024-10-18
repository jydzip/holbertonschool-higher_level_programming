import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'

def fetch_and_print_posts():
    response = requests.get(url)
    response_dict = response.json()
    if response.status_code == 200:
        print(f'Status Code: {response.status_code}')
        for post in response_dict:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get(url)
    if response.status_code == 200:
        response_dict = response.json()

        with open('posts.csv', mode='w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            
            for post in response_dict:
                csv_writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
