#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        self.is_new_instance = True
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    self.id = str(uuid.uuid4)
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                self.is_new_instance = False
        if self.is_new_instance:
            storage.new(self)

        def __str__(self):
            return f"[{self.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            self.updated_at = datetime.now()
            storage.save()

        def to_dict(self):
            model_dict = self.__dict__.copy()
            model_dict['__class__'] = self.__class__.__name__
            model_dict['created_at'] = self.created_at.isoformat()
            model_dict['updated_at'] = self.updated_at.isoformat()
            return model_dict
