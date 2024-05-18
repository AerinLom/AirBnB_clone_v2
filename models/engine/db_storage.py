#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    '''database storage engine for MySQL storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate new DBStorage instance'''
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        hbnb_env = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                mysql_user,
                mysql_pwd,
                mysql_host,
                mysql_db
            ), pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query objects from database """
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj
        else:
            for cls_instance in classes.values():
                objs = self.__session.query(cls_instance).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Add object to current database session """
        if obj:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """ Commit changes to current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session """
        if obj:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """ Create all tables in the database and create a new session """
        Base.metadata.create_all(self.__engine)
        session_creation = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        self.__session = scoped_session(session_creation)()

    def close(self):
        """Closes the working SQLAlchemy session"""
        self.__session.close()
