#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


#Base = declarative_base()

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id """
        from models import storage
        from models.city import City
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]
