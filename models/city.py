#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class for representing a city.

    Attributes:
        state_id (str): The state id to which the city belongs.
        name (str): The name of the city.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
