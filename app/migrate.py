import os
import json
from app.db import db
from app import models


def load_data(file_path):
    """
    Загружает содержимое файлов с данными
    :param file_path: путь до файла
    :return: содержимое файла или пустой список
    """
    data = []
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    return data


def migrate_user_roles(data_path):
    data_from_file = load_data(data_path)

    for role in data_from_file:
        if db.session.query(models.UserRole).filter(models.UserRole.id == role['id']).first() is None:
            new_role = models.UserRole(**role)
            db.session.add(new_role)

    db.session.commit()


def migrate_users(data_path):
    data_from_file = load_data(data_path)

    for user in data_from_file:
        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            new_user = models.User(**user)
            db.session.add(new_user)

    db.session.commit()
