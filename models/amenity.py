#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class for representing an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
