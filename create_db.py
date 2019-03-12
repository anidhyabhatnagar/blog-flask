# The function create_all() in create_db.py module will autmaticall look at
# all the code that we have written and create a new table in our database
# for the Entry model based on our models.

import os, sys
sys.path.append(os.getcwd())
from main import db

if __name__ == '__main__':
    db.create_all()

