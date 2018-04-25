'''
database.credentials
~~~~~~~~~~~~~~~~~~~~~~
Module contains the database credentials needed to connect with the database

'''

import os


DB_URL = os.getenv('APP_DATABASE_URL')
DB_NAME = os.getenv('APP_DATABASE_NAME')
DB_USER = os.getenv('APP_DATABASE_USER')
DB_PASSWORD = os.getenv('APP_DATABASE_PASSWORD')


def get_data_uri():
    """
    Function returns the database uri for Postgres to connect.

    Returns
    --------
    str:
        database URI of Postgress.
    """
    return 'postgresql://{}@{}/{}'.format(DB_USER,
                                          DB_URL, DB_NAME)


def get_test_uri():
    """
    Function returns the database uri for Postgres to connect.

    Returns
    --------
    str:
        database URI of Postgress.
    """
    return 'postgresql://{}@{}/{}'.format(DB_USER,
                                          DB_URL, 'testing')
