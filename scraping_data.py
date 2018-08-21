#!/usr/bin/env python

#Python 2.7

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


url = 'https://www.vistaprint.com/business-cards?txi=18264&xnid=AllProductsPage_Business+cards_All+Products&xnav=AllProductsPage&GP=08%2f21%2f2018+14%3a52%3a04&GPS=5146966587&GNF=0'
cardsurl = requests.get(url)
soup = BeautifulSoup(cardsurl.content, 'lxml')

# div tag for the steps of creating bussiness cards
div = soup.find("div", {"class" : "grid-container grid-container-line-wrap"})


# GETTING ALL INFORMATION FROM THE PRODUCTS

# BANNER TAGS
banner_tag = div.find_all("strong")
just_banner = [banner.get_text().strip() for banner in banner_tag]



name_tag = div.find_all("p", class_="standard-product-tile-name")
just_name = [ name.get_text().strip() for name in name_tag]

description_tag = div.find_all("div", class_="standard-product-tile-description")
just_descriptions = [des.get_text().strip() for des in description_tag]

pricing_tag = div.find_all("div", class_="standard-product-tile-pricing")
just_pricing = [price.get_text().strip() for price in pricing_tag]

normal_tag = div.find_all(class_="comparative-list-price")
just_normal = [normal.get_text().strip() for normal in normal_tag]

discount_tag = div.find_all(class_="discount-price")
just_discount = [discount.get_text().strip() for discount in discount_tag]



# print(just_banner)
# print("-------------------------------------")
# print(just_name)
# print("-------------------------------------")
# print(just_descriptions)
# print("-------------------------------------")
# print(just_pricing)
# print("-------------------------------------")
# print(just_normal)
# print("-------------------------------------")
# print(just_discount)




print("___________________________________________________________________________")

businesscards = ({

			"name" 			: just_name,
			"description" 	: just_descriptions,
			"pricing" 		: just_pricing,
			"normal" 		: just_normal,
			"discount" 		: just_discount
			})

# BCS ARRAYS IS NOT IN THE SAME LENGTH
df = pd.DataFrame.from_dict(businesscards, orient='index')
df_result = df.transpose()

# REORDERING COLOUMNS
label_arr = df_result[[ 'name', 'description', 'pricing', 'normal', 'discount' ]]

print(label_arr)

label_arr.to_csv('bussiness_card_list_final.csv', index_label=None )





################################################################################
# SHAPE FOR THE BUSSINESS CARDS
# steps of shaping the bussiness cards
# from HTML file
# row = index[0]


# row = div.find_all("div", class_="row")

# tile_name = row.find(class_="standard-product-tile-name").get_text().strip()
# tile_des = row.find(class_="standard-product-tile-description").get_text().strip()
# tile_pricing = row.find("div", class_="standard-product-tile-pricing").get_text().strip()
# tile_normal = row.find(class_="comparative-list-price").get_text()
# tile_discount = row.find(class_="discount-price").get_text()

# print(tile_name)
# print(tile_des)
# print(tile_pricing)
# print(tile_normal)
# print(tile_discount)

#  FINDING ALL THE FIRST PRODUCTS IN LIST COMPREHENSION
# names 			= [name.get_text().strip() for name in row.select(".standard-product-tile-name") ]
# descriptions 		= [des.get_text().strip() for des in row.find_all(class_="standard-product-tile-description") ]
# pricings 			= [price.get_text().strip() for price in row.find_all(class_="standard-product-tile-pricing") ]
# normals 			= [normal.get_text().strip() for normal in row.find_all(class_="comparative-list-price") ]
# discounts 		= [discount.get_text().strip() for discount in row.find_all(class_="discount-price") ]

# print(names)
# print(descriptions)
# print(pricings)
# print(normals)
# print(discounts)
