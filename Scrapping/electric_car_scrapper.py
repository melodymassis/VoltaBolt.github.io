###Import Libraries
#Selenium - Chrome Driver to Scrape Web Pages 
#Beautiful Soup - Web Scrapper 
#Requests - Get/Post informaton fetching using URLs
#Pandas - For Data handling and analysis
#pymongo - Database
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo


def scrapper_main():
    plugin_america_website_soup = fetch_information()
    car_model = get_car_model(plugin_america_website_soup)
    car_company = get_car_company(plugin_america_website_soup)
    car_description = get_car_description(plugin_america_website_soup)
    car_range = get_car_range(plugin_america_website_soup)
    car_seats = get_car_seats(plugin_america_website_soup)
    car_price = get_car_price(plugin_america_website_soup)
    car_image_url = get_car_images(plugin_america_website_soup)
    car_information = get_car_information(car_model,car_company,car_description,car_range,car_seats,car_price,car_image_url)
    database_integration(car_information)
    return car_information

##Selenium Chrome Driver Set Up
###Two Coders with different Paths to the Executable file
def fetch_information():
    ###Yamini's Driver Path
    #Commented when used by Pratham Doshi
    #driver= webdriver.Chrome('C:/Users/renuka/Desktop/chromedriver.exe')

    #Pratham's Driver Path
    #Commented when used by Yamini
    driver = webdriver.Chrome('/Users/prathamdoshi/Desktop/chromedriver')

    driver.get("https://pluginamerica.org/vehicles/?fwp_type=ev")
    information = BeautifulSoup(driver.page_source,"lxml")
    driver.quit()
    return information

##Get Car Model
###Takes in a Bs4 object and parses it to extract information
def get_car_model(plugin_america_website_soup):
    #html object that has all the car models listed
    car_models_list_html = plugin_america_website_soup.find_all('td', class_="make_model sorting_1")

    #Extracting the company name and the model out of the html object
    temp = []

    for model_make in car_models_list_html:
        model_make_text_string = model_make.text
        temp.append(model_make_text_string)
    return temp

##Get Car Company
###Takes in a Bs4 object and parses it to extract information
def get_car_company(plugin_america_website_soup):
    #html object that has all the car models listed
    car_models_list_html = plugin_america_website_soup.find_all('td', class_="make_model sorting_1")

    #Extracting the company name and the model out of the html object
    temp = []

    for model_make in car_models_list_html:
        model_make_text_string = model_make.text
        model_make_string_splitter = model_make_text_string.split(' ',1)
        temp.append(model_make_string_splitter[0])
    return temp

##Get Car Description
###Takes in a Bs4 object and parses it to extract information
def get_car_description(plugin_america_website_soup):
    #html object that has all the car descriptions listed
    car_description_list_html = plugin_america_website_soup.find_all('td', class_="car_description")

    #Extracting the company name and the model out of the html object
    temp = []

    for description in car_description_list_html:
        description_text_string = description.p.text
        temp.append(description_text_string)
    return temp

##Get Car Range
###Takes in a Bs4 object and parses it to extract information
def get_car_range(plugin_america_website_soup):
    #html object that has all the car ranges listed
    car_range_list_html = plugin_america_website_soup.find_all('td', class_="car_range")

    #Extracting the company name and the model out of the html object
    temp = []

    for range_ in car_range_list_html:
        range_text_string = range_.p.text
        range_text_string = range_text_string.rstrip().replace('\t', '')
        temp.append(range_text_string)
    return temp

##Get Number of Seats
###Takes in a Bs4 object and parses it to extract information
def get_car_seats(plugin_america_website_soup):
    #html object that has number of seats in a car listed
    car_seats_list_html = plugin_america_website_soup.find_all('td', class_="number_of_seats")

    #Extracting the number of seats out of the html object
    temp = []

    for seats in car_seats_list_html:
        seats_text_string = seats.p.text
        temp.append(seats_text_string)
    return temp

##Get Car Price
###Takes in a Bs4 object and parses it to extract information
def get_car_price(plugin_america_website_soup):
    #html object that has car prices listed
    car_prices_list_html = plugin_america_website_soup.find_all('td', class_="car_price")

    #Extracting the car price out of the html object
    temp = []

    for price in car_prices_list_html:
        price_text_string = price.p.text
        price_text_string = price_text_string.rstrip().replace('\t', '')
        price_text_string = price_text_string.rstrip().replace('  ', '')
        temp.append(price_text_string)
    return temp

##Get Car Images
###Takes in a Bs4 object and parses it to extract information
def get_car_images(plugin_america_website_soup):
    #html object that has car images URL listed
    car_images_list_html = plugin_america_website_soup.find_all('td', class_="car_img")

    #Extracting the company name and the model out of the html object
    temp = []

    for url in car_images_list_html:
        temp.append((url.a.attrs['href']))
    return temp

##Get Car Information
###Combines all the the information scrapped
def get_car_information(car_model,car_company,car_description,car_range,car_seats,car_price,car_image_url):
    temp = []
    cars_information_appender = dict()
    for i in range(len(car_company)):
        cars_information_appender = {
                                     car_model[i] : 
                                                    {
                                                        'Company':car_company[i],
                                                        "Image URL":car_image_url[i],
                                                        'Description':car_description[i],
                                                        'Price':car_price[i],
                                                        'Range':car_range[i],
                                                        'Number of Seats':car_seats[i]                          
                                                    } 
                                    }
        temp.append(cars_information_appender)
    return temp
##Databse Integration - Database Name : Cars_DB, Collection Name: Cars
###Integrates the data in locally hosted mongodb
def database_integration(car_information):
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.Cars_DB
    collection = db.Cars

    #collection insert
    collection.insert_many(car_information)

print(scrapper_main())
