import json
from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):

    def test_successful_creation(self):
        # Given
        email = "paurakh011@gmail.com"
        password = "mycoolpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        self.app.post('/api/v1/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/v1/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        movie_payload = {
            "name": "Star Wars: The Rise of Skywalker",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        }
        # When
        response = self.app.post('/api/v1/movies',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(movie_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
