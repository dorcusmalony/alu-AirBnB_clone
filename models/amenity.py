from models.base_model import BaseModel


class Amenity(BaseModel):

  def __init__(self):
    self.name = ""
    super().__init__()
