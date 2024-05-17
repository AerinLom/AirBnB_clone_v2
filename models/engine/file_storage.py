#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage,
        optionally filtered by class type.

        Args:
            cls (str, optional): The class name to filter by.
                Defaults to None (return all objects).

        Returns:
            dict: A dictionary containing all objects or objects
                of the specified class.
        """
        if cls is not None:
            object_dict = {}
            for k, v in self.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    object_dict[k] = v
            return object_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp_data = {}
            temp_data.update(FileStorage.__objects)
            for key, val in temp_data.items():
                temp_data[key] = val.to_dict()
            json.dump(temp_data, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage (if present)

        Args:
            obj (object, optional): The object to delete.
                If None, no deletion occurs.
        """

        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls the reload method to close"""
        self.reload()
