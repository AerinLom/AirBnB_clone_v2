#!/usr/bin/python3
"""
This module instantiates which storage is used
"""
from os import getenv

specified_storage = getenv('HBNB_TYPE_STORAGE')

if specified_storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif specified_storage == 'fs':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
