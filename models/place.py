#!/usr/bin/python3
"""This module defines a class Place for the HBNB project"""
from models.base_model import BaseModel

class Place(BaseModel):
    """A class representing a place to stay"""

    # Place attributes
    city_id = ""             # ID of the associated City
    user_id = ""             # ID of the associated User
    name = ""                # Name of the place
    description = ""         # Description of the place
    number_rooms = 0         # Number of rooms in the place
    number_bathrooms = 0     # Number of bathrooms in the place
    max_guest = 0            # Maximum number of guests allowed
    price_by_night = 0       # Price per night for the place
    latitude = 0.0           # Latitude coordinate of the place
    longitude = 0.0          # Longitude coordinate of the place
    amenity_ids = []         # List of IDs of associated amenities

