# REST API Python Backend Server

## Table of Contents
- [About](#About)
- [Tech Stack](#Tech-Stack)
- [Local Setup](#Local-Setup)
- [Running the Server Locally](#Running-the-Server-Locally)
- [Running Tests](#Running-Tests)
- [Schema](#Schema)
- [Interacting with Database](#Interacting-with-Database)
- [Endpoint Documentation](#Endpoint-Documentation)
- [Thanks](./license.txt)

## About

This REST API backend server implements an OOP (Object-Oriented Programming) and SRP (Single-Responsibility Principle) patterned code using `Python` for language, `Flask` as our web framework, `MongoDB` as our database, and `unittest` as our testing framework.

This server exposes endpoints for a Movie Model as well as a User Model using Authentication and applying Authorization safeguards on the User endpoint code.

## Tech Stack
- [Python3](https://www.python.org)
  - `pip` (package manager)
  - `pipenv` (virtual environment)
- [Flask](https://palletsprojects.com/p/flask/)
  - Flask Extensions:
    - MongoEngine
    - RESTful
    - Bcrypt
    - JWT
    - Mail
- [MongoDB](https://www.mongodb.com)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Local Setup
- Initial Requirements:
  - [Python, Pip, and Pipenv](https://github.com/priyapower/priya_and_ricky_learn_python/blob/main/lessons/1setup.md)
- [Clone](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) down this repo
  - What is automatically loaded:
    - PyPi
    - Flask + extensions:
      - flask-mongoengine
      - flask-restful
      - flask-bcrypt
      - flask-jwt-extended
      - flask-mail
- Create a `.env` file at the root of the project directory (you may make a `.env.test` or a `.env.prod` or even a `.env.dev` depending on how you determine your environments):
  ```c
  JWT_SECRET_KEY = '<any-random-string/phrase/key>'
  MAIL_SERVER = "localhost"
  MAIL_PORT = "1025"
  MAIL_USERNAME = "support@practice-api-movies.com"
  MAIL_PASSWORD = ""

  MONGODB_SETTINGS = {
      'host': 'mongodb://localhost/practice-api-movies'
  }
  ```
- Install mongo (the following is for [mac](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/), please see mongo docs for [windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) of [linux](https://docs.mongodb.com/manual/administration/install-on-linux/) installation):
  - `brew tap mongodb/brew`
  - `brew install mongodb-community@4.4` (you can replace 4.4 with whatever version you need)
- Need to change your local port?
  - In `run.py`:
    ```py
    # OLD
    app.run()

    # NEW
    app.run(port=<port-you-declare>)
    ```
- Deployed? Need to update from local to your deployed site? Check out this [tutorial](https://towardsdatascience.com/deploying-a-flask-app-on-heroku-and-connecting-it-to-mongodbs-mlab-e0022c4e6d1e)

## Running the Server Locally
- Run `pipenv shell` to enter the virtual environment
- Export the environment you are going to use:
  - **DEV** (if this is `.env`)
    - Mac: `export ENV_FILE_LOCATION=./.env`
    - Windows: `set ENV_FILE_LOCATION=./.env`
  - **TEST** (if this is `.env.test`)
    - Mac: `export ENV_FILE_LOCATION=./.env.test`
    - Windows: `set ENV_FILE_LOCATION=./.env.test`
- You will need 2 terminal tabs open at the root directory:
  - Tab 1 (the be server): `python run.py`
  - Tab 2 (the mail server): run `python -m smtpd -n -c DebuggingServer localhost:1025`
- For [endpoints](#endpoint-documentation), see below.

## Running Tests
- This uses [`unittest`](https://docs.python.org/3/library/unittest.html) which is a Python native testing framework
- To run the full test suite, `python -m unittest -b`
- To run a single test, run `python -m unittest tests/test_name-of-test.py`

## Schema
![This Schema](https://user-images.githubusercontent.com/49959312/103467692-da2a0580-4d0e-11eb-8dc8-a5566a355093.png)

## Interacting with Database
- You can always add data using Postman, see [endpoint documentation](#endpoint-documentation)
- You can also interact with the database through the GUI (such as [Mongo Compass](https://www.mongodb.com/products/compass))
- However, this section will cover using [Mongo Shell](https://docs.mongodb.com/manual/mongo/)
- Mongo Shell [commands](https://docs.mongodb.com/manual/reference/mongo-shell/)
- Helpful reminder, make sure you know what environment you are in!
  - _For example_, In the sequence below, I added dummy data to my `practice-api-movies`. which is my _dev_ environment.
  - But when I booted up my server, my export ENV was still in my _test_ environment, as declared in my `.env.test` file.
  - Which meant all my interactions with postman (in endpoint documentation below) were with the database `practice-api-movies-test`.
  - This made me pause until I remembered I was in 2 distinct environments, therefore 2 distinct databases!
- To run mongo from terminal, enter `mongo`
  - You should see a response similar to:
    ```console
    MongoDB shell version v4.4.3
    connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
    Implicit session: session { "id" : UUID("0196dce6-8772-46e1-ae2d-4f4cfbe310f5") }
    MongoDB server version: 4.4.3
    ...
    ...
    >
    ```
  - To exit, use CTRL + C
- **Example sequence** for adding dummy data:
  1. See the databases you have
    ```py
    show dbs
    ```
    - If you don't see your db name, that's okay, step #2 will take care of that
  2. Access your database
    ```py
    use practice-api-movies
    ```
    - This will both access AND create a database
    - You can always name your db something different, but make sure to update the db name in your host code, see `.env` file under [local setup](#local-setup))
  3. See the collections you have
    ```py
    show collections
    ```
    - If you don't have any collections, that's okay, step #4 will take care of that
  4. Insert some users (this also creates the collection `user` at the same time)
    ```py
    db.user.insert([
      {
        "email": "AnnieAlgebra@test.com",
        "password": "PassyPassword"
      },
      {
        "email": "ConnieCalculus@test.com",
        "password": "IAmAPassword"
      }
    ])
    ```
  5. See your users and grab their `id` for the `added_by` field in Movie
    ```py
    db.user.find().pretty()
    ```
    - RESPONSE (you will need to copy these ids for #6)
    ```py
    {
    	"_id" : ObjectId("5ff0e4e068622519535b948d"),
    	"email" : "AnnieAlgebra@test.com",
    	"password" : "PassyPassword"
    }
    {
    	"_id" : ObjectId("5ff0e4e068622519535b948e"),
    	"email" : "ConnieCalculus@test.com",
    	"password" : "IAmAPassword"
    }
    ```

  6. The first 2 records belong to Annie and the last record belongs to Connie
    ```py
    db.movie.insert([
      {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"],
        "added_by": ObjectId("5ff0e4e068622519535b948d")
      },
      {
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"],
        "added_by": ObjectId("5ff0e4e068622519535b948d")
      },
      {
        "name": "The Dark Knight",
        "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"],
        "added_by": ObjectId("5ff0e4e068622519535b948e")
      }
    ])
    ```
    - Take note that for the `added_by` field, I have pasted in the user id's from the response in #5
  7. Some other commands you may need:
    ```py
    db.dropDatabase()
    db.user.find().pretty()
    db.movie.find().pretty()
    db.user.update({"id": ObjectId(..)}, {"field": "UPDATE"})
    db.movie.update({"id": ".."}, {"field": "UPDATE"})
    db.user.remove({"id": ObjectId(..)})
    db.movie.remove({"id": ".."})
    ```

## Endpoint Documentation
------------
#### Users
------------
- **User Signup**
  - GET `/api/v1/auth/signup`
  - Registers a new user
  - Example call:
    - GET `http://localhost:5000/api/v1/auth/signup`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body:
    ```json
    {
        "email": "PostmanExample@postman.com",
        "password": "IAmAnExample"
    }
    ```
  - ![User signup](https://user-images.githubusercontent.com/49959312/103468006-2aef2d80-4d12-11eb-996a-e6fc2dc59a2e.png)
- **User Login**
  - GET `/api/v1/auth/login`
  - Logs in a user and returns the `web-token`
  - Example call:
    - GET `http://localhost:5000/api/v1/auth/login`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body:
    ```json
    {
        "email": "PostmanExample@postman.com",
        "password": "IAmAnExample"
    }
    ```
  - ![User login](https://user-images.githubusercontent.com/49959312/103468024-570aae80-4d12-11eb-9036-095a83c9cf2c.png)
- **Forgot Password**
  - GET `/api/v1/auth/forgot`
  - Sends an email to the user that sends a reset link with `reset-token` that expires within 24 hours
  - **This requires your SMTP server to be up and running as well.** See [running the server locally](#Running-the-Server-Locally).
  - Example call:
    - GET `http://localhost:5000/api/v1/auth/forgot`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body:
    ```json
    {
        "email": "PostmanExample@postman.com"
    }
    ```
  - For Postman users, click on `authorization`, and then click on `bearer token` in the drop down
  - Paste your token from **`login`** endpoint return
  - Body = ![Forgot password BODY](https://user-images.githubusercontent.com/49959312/103468096-dac49b00-4d12-11eb-98d2-1931ae47495e.png)
  - Authorization = ![Forgot password AUTH](https://user-images.githubusercontent.com/49959312/103468120-17909200-4d13-11eb-814c-d7a1547d6d7d.png)
  - Mail Confirmation = ![Forgot password MAIL](https://user-images.githubusercontent.com/49959312/103468130-2d05bc00-4d13-11eb-9954-56d3a306c4cf.png)
- **Reset Password**
  - GET `/api/v1/auth/reset`
  - If the correct `reset-token` is input, this resets a users password and then sends a confirmation email with the body: "Password reset was successful"
  - **This requires your SMTP server to be up and running as well.** See [running the server locally](#Running-the-Server-Locally).
  - Example call:
    - GET `http://localhost:5000/api/v1/auth/reset`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body:
    ```json
    {
        "password": "ResetPasswordExample",
        "reset_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDk2MjgxNjYsIm5iZiI6MTYwOTYyODE2NiwianRpIjoiOWY3Yzk1YmUtZTUzNC00Mjk3LWE5N2YtZjYzODFkMWQxZGQ2IiwiZXhwIjoxNjA5NzE0NTY2LCJpZGVudGl0eSI6IjVmZjBmODY0NWY4ZWFjNDYyMDQ3Yjk4MSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ejBC2EPIx4jDoUz_3cXNHett0e6Uihi4_KhRHGSj70c"
    }
    ```
  - Body = ![Reset password BODY](https://user-images.githubusercontent.com/49959312/103468175-c503a580-4d13-11eb-99a7-41605aa871c2.png)
  - Mail Confirmation = ![Reset password MAIL](https://user-images.githubusercontent.com/49959312/103468179-cfbe3a80-4d13-11eb-8c3d-a4a267c64229.png)

------------
#### Movies
------------
- **GET all Movies**
  - GET `/api/v1/movies`
  - Retrieves all movie records on file, no matter your authorization level
  - Example call:
    - GET `http://localhost:5000/api/v1/movies`
  - ![Get movies](https://user-images.githubusercontent.com/49959312/103468373-aacac700-4d15-11eb-982f-2cafa7854907.png)
  - For this example, I loaded:
    - `user1: 5ff0f8645f8eac462047b981` with 3 movies
    - `user2: 5ff0fde5385ebc3c97ad32b5` with 2 movies
    - Check it out in the `added_by` field below
  ```json
    [
        {
            "_id": {
                "$oid": "5ff0fd6d385ebc3c97ad32b2"
            },
            "name": "The Shawshank Redemption",
            "casts": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton",
                "William Sadler"
            ],
            "genres": [
                "Drama"
            ],
            "added_by": {
                "$oid": "5ff0f8645f8eac462047b981"
            }
        },
        {
            "_id": {
                "$oid": "5ff0fdd7385ebc3c97ad32b3"
            },
            "name": "Movie 2",
            "casts": [
                "Cast1",
                "Cast2"
            ],
            "genres": [
                "Genre"
            ],
            "added_by": {
                "$oid": "5ff0f8645f8eac462047b981"
            }
        },
        {
            "_id": {
                "$oid": "5ff0fddb385ebc3c97ad32b4"
            },
            "name": "Movie 3",
            "casts": [
                "Cast1",
                "Cast2"
            ],
            "genres": [
                "Genre"
            ],
            "added_by": {
                "$oid": "5ff0f8645f8eac462047b981"
            }
        },
        {
            "_id": {
                "$oid": "5ff0fe20385ebc3c97ad32b6"
            },
            "name": "Movie 15",
            "casts": [
                "Cast1",
                "Cast2"
            ],
            "genres": [
                "Genre"
            ],
            "added_by": {
                "$oid": "5ff0fde5385ebc3c97ad32b5"
            }
        },
        {
            "_id": {
                "$oid": "5ff0fe23385ebc3c97ad32b7"
            },
            "name": "Movie 16",
            "casts": [
                "Cast1",
                "Cast2"
            ],
            "genres": [
                "Genre"
            ],
            "added_by": {
                "$oid": "5ff0fde5385ebc3c97ad32b5"
            }
        }
    ]
  ```
- **GET Movie by Id**
  - GET `/api/v1/movies/<id>`
  - Retrieves a _single_ movie, by id, no matter your authorization level
  - Example call:
    - GET `http://localhost:5000/api/v1/movies/5ff0fe23385ebc3c97ad32b7`
  - ![Get single movie](https://user-images.githubusercontent.com/49959312/103468477-81f70180-4d16-11eb-9e66-bf313ccb03a1.png)
- **Create Movie**  
  - POST `/api/v1/movies`
  - An _authorized_ user may create a new movie record. You must be registered and it will require the users web token for authorization.
  - Example call:
    - POST `http://localhost:5000/api/v1/movies`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body:
    ```json
    {
    	"name" : "The Shawshank Redemption",
    	"casts" : ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    	"genres" : ["Drama"]
    }
    ```
  - For Postman users, click on `authorization`, and then click on `bearer token` in the drop down
  - Paste your token from **`login`** endpoint return
  - Body = ![Create movie](https://user-images.githubusercontent.com/49959312/103468318-1a8c8200-4d15-11eb-9df7-a2b3d3870de9.png)
  - Authorization = ![Create movie Authorization](https://user-images.githubusercontent.com/49959312/103468321-2c6e2500-4d15-11eb-8741-352a84c665a5.png)
- **Update Movie**  
  - PUT `/api/v1/movies/<id>`
  - An _authorized_ user may update _their_ movie record. You must be registered and it will require the users web token for authorization. You will **not** have access to update movies that are not tied to your user id.
  - Example call:
    - PUT `http://localhost:5000/api/v1/movies/5ff0fe23385ebc3c97ad32b7`
  - For Postman users, click on `body`, click on `raw`, and then click `JSON` in the drop down
  - Body
    ```json
    {
        "name": "Python: The Reckoning",
        "casts": ["Priya Power", "Ricky Power"],
        "genres": ["Pew-pew-pew", "Ha-ha-ha", "Smoochy-smooch", "Waaaah-waah", "Dun-dun-duunnnn"]
    }
    ```
  - For Postman users, click on `authorization`, and then click on `bearer token` in the drop down
  - Paste your token from **`login`** endpoint return
  - Body = ![Update movie Body](https://user-images.githubusercontent.com/49959312/103468604-20d02d80-4d18-11eb-900b-4fb085f81c57.png)
  - Authorization = ![Update movie Authorization](https://user-images.githubusercontent.com/49959312/103468631-4c531800-4d18-11eb-8f3c-a274a0f972bf.png)
  - Confirm with Get by Id = ![Update movie Confirm with Get](https://user-images.githubusercontent.com/49959312/103468625-3e04fc00-4d18-11eb-9f1c-4a793250c8dc.png)
- **Delete Movie**
  - DELETE `/api/v1/movies/<id>`
  - An _authorized_ user may delete _their_ movie record. You must be registered and it will require the users web token for authorization. You will **not** have access to delete movies that are not tied to your user id.
  - Example call:
    - DELETE `http://localhost:5000/api/v1/movies/5ff0fe23385ebc3c97ad32b7`
  - For Postman users, click on `authorization`, and then click on `bearer token` in the drop down
  - Paste your token from **`login`** endpoint return
  - Authorization = ![Delete movie Authorization](https://user-images.githubusercontent.com/49959312/103468691-0ea2bf00-4d19-11eb-9ac4-0b0e541ea21c.png)
  - Confirm with Get by Id = ![Delete movie Confirm with Get](https://user-images.githubusercontent.com/49959312/103468697-1a8e8100-4d19-11eb-8394-39895124a036.png)
