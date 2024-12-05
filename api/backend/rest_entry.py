import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask

from backend.db_connection import db
from backend.marketing_analyst.martketing_routes import marketing
from backend.sysadmin.sysadmin_routes import sysadmin
from backend.advisor.advisor_routes import advisor
from backend.students.student_routes import student

import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    # Configuration for MySQL database using environment variables
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')                # 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD') # 'cs3200'
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')                # 'db'
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))           # 3306
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')                  # 'FreshMeet'


    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    
    app.logger.info('current_app(): registering blueprints with Flask app object.')

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(marketing, url_prefix="/marketing")
    app.register_blueprint(sysadmin, url_prefix="/sysadmin")
    app.register_blueprint(advisor, url_prefix = "/advisor")
    app.register_blueprint(student, url_prefix="/student")
    
    

    # Don't forget to return the app object
    return app

