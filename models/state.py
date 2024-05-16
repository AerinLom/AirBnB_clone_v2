#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import specified_storage
from models.city import City


class State(BaseModel, Base):
    """ A class representing state data """

    __tablename__ = 'states'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        @property
        def cities(self):
            """ Returns the list of City objects from storage linked to the current State """
            city_objs = []
            list_of_cities = models.storage.all(City)
            for city in list_of_cities.values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
