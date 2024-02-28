#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
#from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


#Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False)
    name = Column(String(128), ForeignKey("states"), nullable=False)
    places = relationship("Place", backref="cities")
