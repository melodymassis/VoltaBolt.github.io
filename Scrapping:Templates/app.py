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

    Honda_Model = cars_info[0]['Honda Clarity Electric']['Model']
    Honda_Company = cars_info[0]['Honda Clarity Electric']['Company']
    Honda_Image_Url = cars_info[0]['Honda Clarity Electric']['Image URL']
    Honda_Description = cars_info[0]['Honda Clarity Electric']['Description']
    Honda_Price = cars_info[0]['Honda Clarity Electric']['Price']
    Honda_Range = cars_info[0]['Honda Clarity Electric']['Range']
    Honda_Number_Of_Seats = cars_info[0]['Honda Clarity Electric']['Number of Seats']

    Hyundai_Model = cars_info[0]['Hyundai Ioniq Electric']['Model']
    Hyundai_Company = cars_info[0]['Hyundai Ioniq Electric']['Company']
    Hyundai_Image_Url = cars_info[0]['Hyundai Ioniq Electric']['Image URL']
    Hyundai_Description = cars_info[0]['Hyundai Ioniq Electric']['Description']
    Hyundai_Price = cars_info[0]['Hyundai Ioniq Electric']['Price']
    Hyundai_Range = cars_info[0]['Hyundai Ioniq Electric']['Range']
    Hyundai_Number_Of_Seats = cars_info[0]['Hyundai Ioniq Electric']['Number of Seats']

    Kia_Model = cars_info[0]['Kia Soul EV']['Model']
    Kia_Company = cars_info[0]['Kia Soul EV']['Company']
    Kia_Image_Url = cars_info[0]['Kia Soul EV']['Image URL']
    Kia_Description = cars_info[0]['Kia Soul EV']['Description']
    Kia_Price = cars_info[0]['Kia Soul EV']['Price']
    Kia_Range = cars_info[0]['Kia Soul EV']['Range']
    Kia_Number_Of_Seats = cars_info[0]['Kia Soul EV']['Number of Seats']

    Mercedes_Model = cars_info[0]['Mercedes B250e']['Model']
    Mercedes_Company = cars_info[0]['Mercedes B250e']['Company']
    Mercedes_Image_Url = cars_info[0]['Mercedes B250e']['Image URL']
    Mercedes_Description = cars_info[0]['Mercedes B250e']['Description']
    Mercedes_Price = cars_info[0]['Mercedes B250e']['Price']
    Mercedes_Range = cars_info[0]['Mercedes B250e']['Range']
    Mercedes_Number_Of_Seats = cars_info[0]['Mercedes B250e']['Number of Seats']

    Nissan_Model = cars_info[0]['Nissan LEAF']['Model']
    Nissan_Company = cars_info[0]['Nissan LEAF']['Company']
    Nissan_Image_Url = cars_info[0]['Nissan LEAF']['Image URL']
    Nissan_Description = cars_info[0]['Nissan LEAF']['Description']
    Nissan_Price = cars_info[0]['Nissan LEAF']['Price']
    Nissan_Range = cars_info[0]['Nissan LEAF']['Range']
    Nissan_Number_Of_Seats = cars_info[0]['Nissan LEAF']['Number of Seats']

    Quantya_Model = cars_info[0]['Quantya Strada']['Model']
    Quantya_Company = cars_info[0]['Quantya Strada']['Company']
    Quantya_Image_Url = cars_info[0]['Quantya Strada']['Image URL']
    Quantya_Description = cars_info[0]['Quantya Strada']['Description']
    Quantya_Price = cars_info[0]['Quantya Strada']['Price']
    Quantya_Range = cars_info[0]['Quantya Strada']['Range']
    Quantya_Number_Of_Seats = cars_info[0]['Quantya Strada']['Number of Seats']

    Smart_Model = cars_info[0]['Smart ED']['Model']
    Smart_Company = cars_info[0]['Smart ED']['Company']
    Smart_Image_Url = cars_info[0]['Smart ED']['Image URL']
    Smart_Description = cars_info[0]['Smart ED']['Description']
    Smart_Price = cars_info[0]['Smart ED']['Price']
    Smart_Range = cars_info[0]['Smart ED']['Range']
    Smart_Number_Of_Seats = cars_info[0]['Smart ED']['Number of Seats']

    Tesla3_Model = cars_info[0]['Tesla Model 3']['Model']
    Tesla3_Company = cars_info[0]['Tesla Model 3']['Company']
    Tesla3_Image_Url = cars_info[0]['Tesla Model 3']['Image URL']
    Tesla3_Description = cars_info[0]['Tesla Model 3']['Description']
    Tesla3_Price = cars_info[0]['Tesla Model 3']['Price']
    Tesla3_Range = cars_info[0]['Tesla Model 3']['Range']
    Tesla3_Number_Of_Seats = cars_info[0]['Tesla Model 3']['Number of Seats']

    TeslaS_Model = cars_info[0]['Tesla Model S']['Model']
    TeslaS_Company = cars_info[0]['Tesla Model S']['Company']
    TeslaS_Image_Url = cars_info[0]['Tesla Model S']['Image URL']
    TeslaS_Description = cars_info[0]['Tesla Model S']['Description']
    TeslaS_Price = cars_info[0]['Tesla Model S']['Price']
    TeslaS_Range = cars_info[0]['Tesla Model S']['Range']
    TeslaS_Number_Of_Seats = cars_info[0]['Tesla Model S']['Number of Seats']

    TeslaX_Model = cars_info[0]['Tesla Model X']['Model']
    TeslaX_Company = cars_info[0]['Tesla Model X']['Company']
    TeslaX_Image_Url = cars_info[0]['Tesla Model X']['Image URL']
    TeslaX_Description = cars_info[0]['Tesla Model X']['Description']
    TeslaX_Price = cars_info[0]['Tesla Model X']['Price']
    TeslaX_Range = cars_info[0]['Tesla Model X']['Range']
    TeslaX_Number_Of_Seats = cars_info[0]['Tesla Model X']['Number of Seats']

    Victory_Model = cars_info[0]['Victory Empulse TT']['Model']
    Victory_Company = cars_info[0]['Victory Empulse TT']['Company']
    Victory_Image_Url = cars_info[0]['Victory Empulse TT']['Image URL']
    Victory_Description = cars_info[0]['Victory Empulse TT']['Description']
    Victory_Price = cars_info[0]['Victory Empulse TT']['Price']
    Victory_Range = cars_info[0]['Victory Empulse TT']['Range']
    Victory_Number_Of_Seats = cars_info[0]['Victory Empulse TT']['Number of Seats']

    VW_Model = cars_info[0]['Volkswagen e-Golf']['Model']
    VW_Company = cars_info[0]['Volkswagen e-Golf']['Company']
    VW_Image_Url = cars_info[0]['Volkswagen e-Golf']['Image URL']
    VW_Description = cars_info[0]['Volkswagen e-Golf']['Description']
    VW_Price = cars_info[0]['Volkswagen e-Golf']['Price']
    VW_Range = cars_info[0]['Volkswagen e-Golf']['Range']
    VW_Number_Of_Seats = cars_info[0]['Volkswagen e-Golf']['Number of Seats']

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
                            Honda_Model = Honda_Model,
                            Honda_Company = Honda_Company,
                            Honda_Image_Url = Honda_Image_Url,
                            Honda_Description = Honda_Description,
                            Honda_Price = Honda_Price,
                            Honda_Range = Honda_Range,
                            Honda_Number_Of_Seats = Honda_Number_Of_Seats, 
                            Hyundai_Model = Hyundai_Model,
                            Hyundai_Company = Hyundai_Company,
                            Hyundai_Image_Url = Hyundai_Image_Url,
                            Hyundai_Description = Hyundai_Description,
                            Hyundai_Price = Hyundai_Price,
                            Hyundai_Range = Hyundai_Range,
                            Hyundai_Number_Of_Seats = Hyundai_Number_Of_Seats,
                            Kia_Model = Kia_Model,
                            Kia_Company = Kia_Company,
                            Kia_Image_Url = Kia_Image_Url,
                            Kia_Description = Kia_Description,
                            Kia_Price = Kia_Price,
                            Kia_Range = Kia_Range,
                            Kia_Number_Of_Seats = Kia_Number_Of_Seats,
                            Mercedes_Model = Mercedes_Model,
                            Mercedes_Company = Mercedes_Company,
                            Mercedes_Image_Url = Mercedes_Image_Url,
                            Mercedes_Description = Mercedes_Description,
                            Mercedes_Price = Mercedes_Price,
                            Mercedes_Range = Mercedes_Range,
                            Mercedes_Number_Of_Seats = Mercedes_Number_Of_Seats, 
                            Nissan_Model = Nissan_Model,
                            Nissan_Company = Nissan_Company,
                            Nissan_Image_Url = Nissan_Image_Url,
                            Nissan_Description = Nissan_Description,
                            Nissan_Price = Nissan_Price,
                            Nissan_Range = Nissan_Range,
                            Nissan_Number_Of_Seats = Nissan_Number_Of_Seats,  
                            Quantya_Model = Quantya_Model,
                            Quantya_Company = Quantya_Company,
                            Quantya_Image_Url = Quantya_Image_Url,
                            Quantya_Description = Quantya_Description,
                            Quantya_Price = Quantya_Price,
                            Quantya_Range = Quantya_Range,
                            Quantya_Number_Of_Seats = Quantya_Number_Of_Seats, 
                            Smart_Model = Smart_Model,  
                            Smart_Company = Smart_Company,
                            Smart_Image_Url = Smart_Image_Url,
                            Smart_Description = Smart_Description,
                            Smart_Price = Smart_Price,
                            Smart_Range = Smart_Range,
                            Smart_Number_Of_Seats = Smart_Number_Of_Seats,  
                            Tesla3_Model = Tesla3_Model,  
                            Tesla3_Company = Tesla3_Company,
                            Tesla3_Image_Url = Tesla3_Image_Url,
                            Tesla3_Description = Tesla3_Description,
                            Tesla3_Price = Tesla3_Price,
                            Tesla3_Range = Tesla3_Range,
                            Tesla3_Number_Of_Seats = Tesla3_Number_Of_Seats,   
                            TeslaS_Model = TeslaS_Model,  
                            TeslaS_Company = TeslaS_Company,
                            TeslaS_Image_Url = TeslaS_Image_Url,
                            TeslaS_Description = TeslaS_Description,
                            TeslaS_Price = TeslaS_Price,
                            TeslaS_Range = TeslaS_Range,
                            TeslaS_Number_Of_Seats = TeslaS_Number_Of_Seats, 
                            TeslaX_Model = TeslaX_Model,  
                            TeslaX_Company = TeslaX_Company,
                            TeslaX_Image_Url = TeslaX_Image_Url,
                            TeslaX_Description = TeslaX_Description,
                            TeslaX_Price = TeslaX_Price,
                            TeslaX_Range = TeslaX_Range,
                            TeslaX_Number_Of_Seats = TeslaX_Number_Of_Seats,
                            Victory_Model = Victory_Model,  
                            Victory_Company = Victory_Company,
                            Victory_Image_Url = Victory_Image_Url,
                            Victory_Description = Victory_Description,
                            Victory_Price = Victory_Price,
                            Victory_Range = Victory_Range,
                            Victory_Number_Of_Seats = Victory_Number_Of_Seats,      
                            VW_Model = VW_Model,  
                            VW_Company = VW_Company,
                            VW_Image_Url = VW_Image_Url,
                            VW_Description = VW_Description,
                            VW_Price = VW_Price,
                            VW_Range = VW_Range,
                            VW_Number_Of_Seats = VW_Number_Of_Seats         
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