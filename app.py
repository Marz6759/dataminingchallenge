#!/usr/bin/env python3
"""
DATA MINING CHALLENGE
STAGE 2
"""
__author__ = "Marzouq Abedur Rahman"
__version__ = "0.1.0"
__license__ = "CP"

import json
import requests

# Create a temporary bypass for the crawler block on Zalora using agent headers
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/543.36 (KHTML, like Gecko) Chrome/57.0.2924.87 Safari/537.36',
    }

# Get the data from the XHR url and convert response into a json
url = 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?url=%2Fwomen%2Fshoes&sort=popularity&dir=desc&offset=0&limit=400&category_id=4&occasion=Casual&brand=87&gender=women&segment=women&special_price=false&all_products=false&new_products=false&top_sellers=false&catalogtype=Main&lang=en&is_brunei=false&search_suggest=false&enable_visual_sort=true&enable_filter_ads=true&compact_catalog_desktop=false&name_search=false&solr7_support=true&pick_for_you=false&learn_to_sort_catalog=false&is_multiple_source=true'

# Initialise the ID and dictionary for storing each individual shoe
itemID = 0
itemDictionary = dict()

if __name__ == "__main__":
    page = requests.get(url, headers=headers).json()

    # Select the items from the response json
    items = page['response']['docs']

    for item in items:
        # Get the brand, actual price
        brand = item['meta']['brand']
        actualPrice = item['meta']['price']

        # Get the discounted price
        discountedPrice = item['meta']['special_price']
        # If discounted price is empty, replace it with "NO DISCOUNT"
        if discountedPrice == '':
            discountedPrice = 'NO DISCOUNT'

        # Get image link and strip the filler code from the front
        imageLink = item['image']
        imageLink = imageLink[imageLink.find('http://static'):]

        # Add the item to the dictionary
        itemDictionary[str(itemID)] = {
            'brand': brand,
            'actual_price': actualPrice,
            'discounted_price': discountedPrice,
            'image_link': imageLink
        }

        itemID += 1

    # Write dictionary to output json file
    with open("dataminingchallenge.json", "w") as outfile:
        json.dump(itemDictionary, outfile)




