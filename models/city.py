#!/usr/bin/python3
""" City module
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """City class
    """
    state_id = ""
    name = ""
