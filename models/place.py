#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import specified_storage
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models

if specified_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if specified_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review",
                               cascade="all, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if specified_storage != 'db':
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances."""
            from models import storage
            all_reviews = storage.all(Review).values()
            list_of_reviews = [review for review in all_reviews
                               if review.place_id == self.id]
            return list_of_reviews

        @property
        def amenities(self):
            """Getter attribute amenities"""
            from models import storage
            all_amenities = storage.all(Amenity).values()
            list_of_amenities = [amenity for amenity in all_amenities
                                 if amenity.id in self.amenity_ids]
            return list_of_reviews

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute amenities"""
            if amenity is not None and isinstance(amenity, Amenity) \
                    and amenity.id not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)
