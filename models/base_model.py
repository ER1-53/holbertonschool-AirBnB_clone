#!/bin/python3
"""Python console"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class Basemodel"""
    def __init__(self, *args, **kwargs):
        """initialize instance"""
        attributes = ["id", "created_at", "updated_at"]
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """print instances"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the time of the last instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """do a copy of dictionnary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.\
            strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.\
            strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict
