import requests
from bs4 import BeautifulSoup
import json

def find_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any bad response status

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags representing links
        links = soup.find_all('a')

        # Extract the URLs from the href attribute of each link
        link_list = [link.get('href') for link in links if link.get('href')]

        # Construct the JSON object
        result = {url: link_list}

        return json.dumps(result)  # Convert the dictionary to a JSON string

    except requests.RequestException as e:
        return json.dumps({"error": "Error fetching the page: {}".format(e)})
