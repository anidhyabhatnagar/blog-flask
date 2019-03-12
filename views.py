# The views moduel will contain a single view mapped to the root URL of the
# site.

from app import app


@app.route('/')
def homepage():
    return 'Home Page'

