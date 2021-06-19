import click
import re
import requests

BASE_URL = 'https://api.publicapis.org'

@click.group()
def public_apis():
    """A CLI wrapper for the API of Public APIs."""

@public_apis.command()
@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".')
def entry(no_auth: bool, category: str, title: str):
    """List all catagories of the Public APIs."""
    response = requests.get(url=f'{BASE_URL}/categories')
    if response.status_code == 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get the categories: {response.text}')

def generate_query(no_auth, category, title):

    return true


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
        print(f'Could not get the categories: {response.text}')

def find_matching_name(categories, name):
    filtered_categories = []
    for category in categories:
        if re.search(name, category, re.IGNORECASE):
            filtered_categories.append(category)
    
    return filtered_categories

if __name__ == '__main__':
    public_apis(prog_name='public_apis')