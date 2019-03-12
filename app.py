
from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.marsDB

@app.route("/")

def index():
    mars_data = {}
    mars = db.mars.find()
    print(scrape_mars.scrape())
    print("$$$$$$$$$$$$$$$$$")
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars 
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert = True)
    return redirect("http://localhost:27017/")

if __name__ == "__main__":
    app.run(debug=True)