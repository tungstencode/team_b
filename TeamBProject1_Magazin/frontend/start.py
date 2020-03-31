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
    return render_template("index.html", body=data[0]) 

if __name__ == "__main__":
    # Starting the app at http://localhost:8000
    app.run(host='localhost', port=8000)