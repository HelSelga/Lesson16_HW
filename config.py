import os.path

DATA_BASE_DIR = 'data'

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_ROLES_DATA_PATH = os.path.join(DATA_BASE_DIR, 'Users_role.json')
    USER_DATA_PATH = os.path.join(DATA_BASE_DIR, 'Users.json')
