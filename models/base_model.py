#!/usr/bin/python3
"""BaseModel Class  for all models"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """The BaseModel Class for all models"""

    def __init__(self, *arg, **kwarg):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwarg:
            for key, value in kwarg.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Save the BaseModel instance."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        dict_cp = self.__dict__.copy()
        dict_cp["__class__"] = self.__class__.__name__
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        return dict_cp
