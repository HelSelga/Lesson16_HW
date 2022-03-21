import os
import json
from app.db import db
from app import models

from datetime import datetime


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


def migration(data_path, model, convert_date=False):
    """
    Миграция данных в таблицы
    :param data_path: содержимое файлов для загрузки в таблицы
    :param model: модель для конкретной таблицы
    :param convert_date: конвертация дат в формат ISO-8601
    """
    data_from_file = load_data(data_path)

    for data in data_from_file:
        if convert_date:
            for field_name, field_value in data.items():
                if isinstance(field_value, str) and field_value.count('/') == 2:
                    data[field_name] = datetime.strptime(field_value, '%m/%d/%Y').date()

        if db.session.query(model).filter(model.id == data['id']).first() is None:
            db.session.add(model(**data))
    db.session.commit()


def migrate_user_roles(data_path):
    migration(
        data_path=data_path,
        model=models.UserRole,
    )


def migrate_users(data_path):
    migration(
        data_path=data_path,
        model=models.User,
    )


def migrate_orders(data_path):
    migration(
        data_path=data_path,
        model=models.Order,
        convert_date=True
    )


def migrate_offers(data_path):
    migration(
        data_path=data_path,
        model=models.Offer,
    )