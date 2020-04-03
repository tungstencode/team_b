from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index(): 
    URL = "http://localhost:7000/movies"
    # Get Json from url
    r = requests.get(url = URL)   
    # Create an object from json
    data = r.json() 
    # Send the first element in the template
    return render_template("pages/index.html", body=data[0]) 

@app.route("/catalog")
def catalog(): 
    URL = "http://localhost:7000/catalog"
    r = requests.get(url = URL)   
    data = r.json() 
    return render_template("pages/catalog.html", catalog_items=data) 

if __name__ == "__main__":
    # Starting the app at http://localhost:8000
    app.run(host='localhost', port=8000, debug=True)