#!/usr/bin/python3
""" DB Storage Engine """

import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """ Defines the DB Storage """

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the DB Storage """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST"),
            os.environ.get("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session depending on class name """
        objects = {}
        if cls is not None:
            results = self.__session.query(cls).all()
            for obj in results:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = ["Place", "Amenity", "User", "City", "State", "Review"]
            for obj in classes:
                results = self.__session.query(obj).all()
                for record in results:
                    key = "{}.{}".format(type(record).__name__, record.id)
                    objects[key] = record
        return objects

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads the database for persistence """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
