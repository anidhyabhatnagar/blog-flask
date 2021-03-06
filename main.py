# The main moduel is the entry point into our app

from app import app, db
import models
import views
from entries.blueprint import entries


app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

