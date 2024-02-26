#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
import uuid
import json
import os
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel class defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
     from models import storage  # Import locally within a method
     obj_dict = {key: obj.to_dict() for key, obj in storage.all().items()}
     with open(storage._FileStorage__file_path, 'w') as file:
        json.dump(obj_dict, file)

    def reload(self):
     from models import storage  # Import locally within a method
     if os.path.exists(storage._FileStorage__file_path):
        with open(storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj = globals()[class_name](**value)
                storage._FileStorage__objects[key] = obj

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict


if __name__ == "__main__":
    my_model = BaseModel()
