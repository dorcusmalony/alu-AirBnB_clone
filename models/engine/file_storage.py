#!/usr/bin/python3
"""
Write a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances:
"""
from datetime import datetime
import copy
import json


class FileStorage:
    """
    Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by
    <class name>.id (ex: to store a BaseModel object with id=12121212,
    the key will be BaseModel.12121212)
    Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects (only if the
    JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.__dict__

    def reload(self):
        try:
          with open(self.__file_path, "r", encoding="utf-8") as jsfpr:
            self.__objects = json.load(jsfpr)
            for key in self.__objects.keys():
              self.__objects[key]["created_at"] = datetime.fromisoformat(
                  self.__objects[key]["created_at"])
              self.__objects[key]["updated_at"] = datetime.fromisoformat(
                  self.__objects[key]["updated_at"])

        except FileNotFoundError:
          pass

    def save(self):
        try:
          with open(self.__file_path, "w", encoding="utf-8") as jsfps:
            if len(self.__objects) != 1:
              count = 0
              for key in list(self.__objects):
                if (count == len(self.__objects)) or (isinstance(
                    self.__objects[key]["created_at"], str)):
                  break
                self.__objects[key]["created_at"] = self.__objects[key][
                    "created_at"].isoformat()
                self.__objects[key]["updated_at"] = self.__objects[key][
                    "updated_at"].isoformat()
                count += 1
            else:
              key = list(self.__objects)[0]
              if isinstance(self.__objects[key]["created_at"], datetime):
                self.__objects[key]["created_at"] = self.__objects[key][
                    "created_at"].isoformat()
                self.__objects[key]["updated_at"] = self.__objects[key][
                    "updated_at"].isoformat()
            json.dump(self.__objects, jsfps)
        except FileNotFoundError:
          pass
