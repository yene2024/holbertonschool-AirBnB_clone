#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(val, timeFormat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(
            class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict


if __name__ == "__main__":
    my_model = BaseModel()
