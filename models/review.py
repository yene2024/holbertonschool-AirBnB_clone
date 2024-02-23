#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class for representing a review.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
