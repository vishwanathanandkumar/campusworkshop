"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13k8jh4hstbhhas9ag-a.oregon-postgres.render.com",
        database="todo_wtjo",
        user="vishwa",
        password="1hovorh6OGaCkweI2DuKJTvbDArlphgd")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
