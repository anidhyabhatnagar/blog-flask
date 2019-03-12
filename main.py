# The main moduel is the entry point into our app

from app import app, db
import models
import views


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

