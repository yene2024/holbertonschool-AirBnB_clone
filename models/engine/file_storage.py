#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Custom class for file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return FileStorage.__objects

    def new(self, object):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write

        """
        object_class_name = object.__class__.__name__
        key = "{}.{}".format(object_class_name, object.id)
        FileStorage.__objects[key] = object

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        all_objects = FileStorage.__objects
        object_dict = {}
        for obj in all_objects.keys():
            object_dict[obj] = all_objects[obj].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(object_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for obj in object_dict.values():
                    class_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
