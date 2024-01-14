from datetime import datetime
import copy
import json


class FileStorage:

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
