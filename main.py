import requests
import bs4
import os

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def parse_html(html):
    if html is None:
        print("No HTML to parse.")
        return None
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup

url = input("Enter the URL to scrape: ")
html = get_html(url)
soup = parse_html(html)
if soup is not None:
    print(soup.prettify())