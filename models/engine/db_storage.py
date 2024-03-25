#!/usr/bin/python3
"""This module creates a database storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This is the class for the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes an instance of DBStorage"""
        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')
        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{passwd}@{host}/{db}",
                pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session \
(self.__session) all objects"""
        objects = {}
        if cls is None:
            classes = [Base.__subclasses__()]
        else:
            classes = [cls]
        for class_ in classes:
            queries = self.__session.query(class_)
            for query in queries:
                key = f"{query.__class__.__name__}.{query.id}"
                objects[key] = query
        return objects

    def new(self, obj):
        """adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        self.__session.remove()
