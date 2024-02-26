#!/usr/bin/python3
"""
Module for the FileStorage class
"""

import json
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(save_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                class_name, obj_id = key.split('.')
                obj_dict = value
                obj_dict['created_at'] = datetime.strptime(
                    obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                obj_dict['updated_at'] = datetime.strptime(
                    obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                instance = eval(class_name)(**obj_dict)
                FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
