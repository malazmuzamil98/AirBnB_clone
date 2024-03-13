#!/usr/bin/python3
"""Serializes instances to JSON"""
import json


class FileStorage:
    """Serializes instances to JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all serializes objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds a new serialized objects"""
        key = f"{obj.__class__.__name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to a JSON file"""
        dict_obj = {}
        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict_obj, file)

    def reload(self):
        """desrialize the objects"""
        from models.base_model import BaseModel

        Models = {
            'BaseModel': BaseModel
        }
        try:
            with open(FileStorage.__file_path, "r") as f:
                desrialized_objects = json.load(f)
                for desrial_values in desrialized_objects.values():
                    class_name = desrial_values["__class__"]
                    def_class = Models['class_name']
                    self.new(def_class(**desrial_values))
        except FileNotFoundError:
            pass
