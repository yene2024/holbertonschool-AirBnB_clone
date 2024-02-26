#!/usr/bin/python3
"""
Module for the FileStorage class
"""

import json
import os
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: Instance of a class to be stored.
        """
        key = obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes and saves the __objects dictionary to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes and reloads objects from the JSON file into __objects.

        Only reloads if the file exists.
        """
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = globals()[value['__class__']](**value)
                    self.__objects[key] = obj
