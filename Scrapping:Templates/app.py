from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import electric_car_scrapper
import pymongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.Cars_DB
collection = db.Cars


app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    data = electric_car_scrapper.scrapper_main()
    collection.insert_one(data)
    return redirect("http://localhost:5000/search", code=302)

@app.route('/search')
def index2():
    cars_info = db.Cars.find()

    BMW_Model = cars_info[0]['BMW i3']['Model']
    BMW_Company = cars_info[0]['BMW i3']['Company']
    BMW_Image_Url = cars_info[0]['BMW i3']['Image URL']
    BMW_Description = cars_info[0]['BMW i3']['Description']
    BMW_Price = cars_info[0]['BMW i3']['Price']
    BMW_Range = cars_info[0]['BMW i3']['Range']
    BMW_Number_Of_Seats = cars_info[0]['BMW i3']['Number of Seats']

    Chevy_Model = cars_info[0]['Chevrolet Bolt EV']['Model']
    Chevy_Company = cars_info[0]['Chevrolet Bolt EV']['Company']
    Chevy_Image_Url = cars_info[0]['Chevrolet Bolt EV']['Image URL']
    Chevy_Description = cars_info[0]['Chevrolet Bolt EV']['Description']
    Chevy_Price = cars_info[0]['Chevrolet Bolt EV']['Price']
    Chevy_Range = cars_info[0]['Chevrolet Bolt EV']['Range']
    Chevy_Number_Of_Seats = cars_info[0]['Chevrolet Bolt EV']['Number of Seats']
 
    Fiat_Model = cars_info[0]['Fiat 500e']['Model']
    Fiat_Company = cars_info[0]['Fiat 500e']['Company']
    Fiat_Image_Url = cars_info[0]['Fiat 500e']['Image URL']
    Fiat_Description = cars_info[0]['Fiat 500e']['Description']
    Fiat_Price = cars_info[0]['Fiat 500e']['Price']
    Fiat_Range = cars_info[0]['Fiat 500e']['Range']
    Fiat_Number_Of_Seats = cars_info[0]['Fiat 500e']['Number of Seats']

    Ford_Model = cars_info[0]['Ford Focus Electric']['Model']
    Ford_Company = cars_info[0]['Ford Focus Electric']['Company']
    Ford_Image_Url = cars_info[0]['Ford Focus Electric']['Image URL']
    Ford_Description = cars_info[0]['Ford Focus Electric']['Description']
    Ford_Price = cars_info[0]['Ford Focus Electric']['Price']
    Ford_Range = cars_info[0]['Ford Focus Electric']['Range']
    Ford_Number_Of_Seats = cars_info[0]['Ford Focus Electric']['Number of Seats']
    
    return render_template('index_two.html',
                            BMW_Model = BMW_Model,
                            BMW_Company = BMW_Company,
                            BMW_Image_Url = BMW_Image_Url,
                            BMW_Description = BMW_Description,
                            BMW_Price = BMW_Price,
                            BMW_Range = BMW_Range,
                            BMW_Number_Of_Seats = BMW_Number_Of_Seats,
                            Chevy_Model = Chevy_Model,
                            Chevy_Company = Chevy_Company,
                            Chevy_Image_Url = Chevy_Image_Url,
                            Chevy_Description = Chevy_Description,
                            Chevy_Price = Chevy_Price,
                            Chevy_Range = Chevy_Range,
                            Chevy_Number_Of_Seats = Chevy_Number_Of_Seats,
                            Fiat_Model = Fiat_Model,
                            Fiat_Company = Fiat_Company,
                            Fiat_Image_Url = Fiat_Image_Url,
                            Fiat_Description = Fiat_Description,
                            Fiat_Price = Fiat_Price,
                            Fiat_Range = Fiat_Range,
                            Fiat_Number_Of_Seats = Fiat_Number_Of_Seats,
                            Ford_Model = Ford_Model,
                            Ford_Company = Ford_Company,
                            Ford_Image_Url = Ford_Image_Url,
                            Ford_Description = Ford_Description,
                            Ford_Price = Ford_Price,
                            Ford_Range = Ford_Range,
                            Ford_Number_Of_Seats = Ford_Number_Of_Seats,                            
                          )

if __name__ == "__main__":
    app.run(debug=True)
    
    

# @app.route('/home')
# def index2():

#     mars_data = db.mars_data.find()
#     Title = mars_data[0]['Title']
#     Description = mars_data[0]['Description']
#     Weather = mars_data[0]['Weather']
#     Facts = mars_data[0]['Facts']

#     Image_Title_1 = mars_data[0]['Images'][0]['title']
#     Image_Title_2 = mars_data[0]['Images'][1]['title']
#     Image_Title_3 = mars_data[0]['Images'][2]['title']
#     Image_Title_4 = mars_data[0]['Images'][3]['title']
    
#     Image_Url_1 = mars_data[0]['Images'][0]['img_url']
#     Image_Url_2 = mars_data[0]['Images'][1]['img_url']
#     Image_Url_3 = mars_data[0]['Images'][2]['img_url']
#     Image_Url_4 = mars_data[0]['Images'][3]['img_url']


#     return render_template('index.html',
#                             Title = Title,
#                             Description =  Description, 
#                             Weather =  Weather,
#                             Image_Title_1 = Image_Title_1,
#                             Image_Title_2 = Image_Title_2,
#                             Image_Title_3 = Image_Title_3,
#                             Image_Title_4 = Image_Title_4,
#                             Image_Url_1 = Image_Url_1,
#                             Image_Url_2 = Image_Url_2,
#                             Image_Url_3 = Image_Url_3,
#                             Image_Url_4 = Image_Url_4,
#                             Facts = Facts
#                             )