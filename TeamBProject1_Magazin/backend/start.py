from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@app.route('/movies')
def hello():
    # Sending the json version of our list
    return jsonify(movies)

# Post method example, adds a movie to the list that it gets from the body
@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

# Update method example, it updates a movie at the index specified in the url with the body sent
@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

# Delelete method example, it pops the element at the index specified in the url
@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200
    
if __name__ == "__main__":
    # Starting the app at http://localhost:7000
    app.run(host='localhost' ,port=7000)