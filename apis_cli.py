import click
import json
import re
import requests

BASE_URL = 'https://api.publicapis.org'

@click.group()
def public_apis():
    """A CLI wrapper for the API of Public APIs."""

@public_apis.command()
@click.argument('title')
@click.option('-a', '--auth', default='', help='Filter out APIs with required auth')
@click.option('-c', '--category', default='', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
def entry(auth: str, category: str, title: str):
    """uery GET /entries to the Public APIs."""
    ENTRY_API_ENDPOINT = f'{BASE_URL}/entries'
    query_payload = {'auth': auth, 'title': title, 'category': category}
    response = requests.get(ENTRY_API_ENDPOINT, params=query_payload)
    if response.status_code == 200:
        print_response(response)
    else:
        print(f'Could not get the entry from the public API resource: {response.text}')

@public_apis.command()
def random():
    """Query GET /random to the Public APIs."""
    RANDOM_API_ENDPOINT = f'{BASE_URL}/random'
    response = requests.get(url=RANDOM_API_ENDPOINT)
    if response.status_code == 200:
        print_response(response)
    else:
        print(f'Could not get a random result from the public API resource: {response.text}')

def print_response(response):
    parsed = response.json()
    click.echo(json.dumps(parsed, indent=2, sort_keys=True))

@public_apis.command()
@click.option('-n', '--name', default='', help='Name of Category (matches via substring - i.e. "at" would return "cat" and "atlas".')
def category(name: str):
    """List all catagories of the Public APIs."""

    response = requests.get(url=f'{BASE_URL}/categories')
    if response.status_code == 200:
        categories = response.json()
        filtered_categories = find_matching_name(categories, name)
        click.echo('\n'.join(filtered_categories))
    else:
        print(f'Could not get the categories from the public API resource: {response.text}')

def find_matching_name(categories, name):
    filtered_categories = []
    for category in categories:
        if re.search(name, category, re.IGNORECASE):
            filtered_categories.append(category)
    
    return filtered_categories

if __name__ == '__main__':
    public_apis(prog_name='public_apis')