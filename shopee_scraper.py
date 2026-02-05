# Shopee Scraper

import requests
from bs4 import BeautifulSoup

class ShopeeScraper:
    def __init__(self, product_name):
        self.product_name = product_name
        self.base_url = 'https://shopee.com'

    def search_product(self):
        search_url = f'{self.base_url}/search?keyword={self.product_name}'
        response = requests.get(search_url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f'Error fetching search results: {response.status_code}')

    def parse_results(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        products = soup.find_all('div', class_='shopee-search-item-result__item')
        results = []
        for product in products:
            title = product.find('div', class_='yQmmFK _1POlWr').text
            price = product.find('span', class_='_341bDY').text
            results.append({'title': title, 'price': price})
        return results

# Example usage:
if __name__ == '__main__':
    scraper = ShopeeScraper('laptop')
    html_content = scraper.search_product()
    products = scraper.parse_results(html_content)
    print(products)
