#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing a state.

    Attributes:
        name (str): The name of the state.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
