#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import specified_storage


class City(BaseModel, Base):
    """ A class representing city data """

    __tablename__ = 'cities'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place",
                              cascade="all, delete-orphan",
                              backref="city")
    else:
        name = ''
        state_id = ''
