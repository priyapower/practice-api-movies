import json
from tests.BaseCase import BaseCase

class TestGetMovies(BaseCase):
    # Tests that you can make a call for GETing all movies and get a 200 status code return and an empty list (datatype equivelant to array in ruby)
    def test_empty_response(self):
        response = self.app.get('/api/v1/movies')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    # Tests a successful (happy path) for getting movies
    def test_movie_response(self):
        # Given
        email = "paurakh011@gmail.com"
        password = "mycoolpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        movie_payload = {
            "name": "Star Wars: The Rise of Skywalker",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        }
        response = self.app.post('/api/v1/movies',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(movie_payload))

        # When
        response = self.app.get('/api/v1/movies')
        added_movie = response.json[0]

        # Then
        self.assertEqual(movie_payload['name'], added_movie['name'])
        self.assertEqual(movie_payload['casts'], added_movie['casts'])
        self.assertEqual(movie_payload['genres'], added_movie['genres'])
        self.assertEqual(user_id, added_movie['added_by']['$oid'])
        self.assertEqual(200, response.status_code)
