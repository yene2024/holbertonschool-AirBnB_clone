#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing a review.

    Attributes:
        place_id (str): The place id to which the review is associated.
        user_id (str): The user id who wrote the review.
        text (str): The text content of the review.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
