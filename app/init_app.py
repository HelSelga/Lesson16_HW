from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app.models import *
from app.db import db

# db: SQLAlchemy = SQLAlchemy()
# with db.session.begin():


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # app.config['JSON_AS_ASCII'] = False

    db.init_app(app)

    with app.app_context():

        from app import routes
        db.drop_all()
        db.create_all()

        return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
