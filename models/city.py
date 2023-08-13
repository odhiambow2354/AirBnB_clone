#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class with state ID and name"""
    state_id = ""  # Associated state's ID
    name = ""      # City name

