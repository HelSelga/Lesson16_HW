from flask import Flask  # Создание приложения
# from flask_sqlalchemy import SQLAlchemy
from app.models import *
from app.db import db


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

        from app import migrate
        migrate.migrate_user_roles(app.config['USER_ROLES_DATA_PATH'])
        migrate.migrate_users(app.config['USER_DATA_PATH'])

        return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
