from .movie import MoviesApi, MovieApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/v1/movies')
    api.add_resource(MovieApi, '/api/v1/movies/<id>')

    api.add_resource(SignupApi, '/api/v1/auth/signup')
    api.add_resource(LoginApi, '/api/v1/auth/login')

    api.add_resource(ForgotPassword, '/api/v1/auth/forgot')
    api.add_resource(ResetPassword, '/api/v1/auth/reset')
