
import Flask
import pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.marsDB

@app.route("/")
def index():
    mars = db.mars.find()
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scrape():
    mars = client.db.mars 
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data)
    return "Scraped data"

if __name__ == "__main__":
    app.run()