#!/usr/bin/python3
"""
Module containing the FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    # Add a class name to class mapping
    __class_name_mapping = {
        'User': User,
        'BaseModel': BaseModel,
        # Add other classes if needed
    }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key in FileStorage.__objects:
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key in obj_dict:
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['__class__'] = class_name
                    # Use the mapping to get the class
                    obj_class = FileStorage.__class_name_mapping.get(class_name, BaseModel)
                    obj_instance = obj_class(**obj_dict[key])
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
