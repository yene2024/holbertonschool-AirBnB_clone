#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()
my_model = BaseModel()
my_model.save()