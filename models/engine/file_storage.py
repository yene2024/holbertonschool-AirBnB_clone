#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Adds a new object to the storage dictionary
        """
        obj_cls_name = obj.__class__.__name__
        key = f"{obj_cls_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns the storage dictionary
        """
        return FileStorage.__objects

    def save(self):
        """Saves the storage dictionary to a file
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads the storage dictionary from the file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except FileNotFoundError:
                    print("** File Not Found **")
