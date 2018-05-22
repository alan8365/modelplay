from django.apps import AppConfig
from django.db import connection
from .models import *

class CurriculumConfig(AppConfig):
    name = 'curriculum'

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM curriculum_course")
        row = cursor.fetchone()

    return row

def sql_to_dict(raw):
    result = dict()

    #list
    columns = raw.colums


