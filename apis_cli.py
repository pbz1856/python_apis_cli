import click
import json
import re
import requests

BASE_URL = 'https://api.publicapis.org'

@click.group()
def public_apis():
    """A CLI wrapper for the API of Public APIs."""

@public_apis.command()
@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title_name', default='', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
@click.option('-c', '--category', default='', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
def get(no_auth: bool, entry_name: str, title: str):
    """Query GET /entries to the Public APIs."""
    ENTRY_URL = f'{BASE_URL}/entries'
    response = requests.get(url=f'{BASE_URL}/{ENTRY_ENDPOINT}')
    if response.status_code == 200:
        print_response(response)
    else:
        print(f'Could not get the categories: {response.text}')

@public_apis.command()
def random():
    """Query GET /random to the Public APIs."""
    ENTRY_URL = f'{BASE_URL}/random'
    response = requests.get(url=ENTRY_URL)
    if response.status_code == 200:
        print_response(response)
    else:
        print(f'Could not get the categories: {response.text}')

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