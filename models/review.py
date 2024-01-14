from models.base_model import BaseModel


class Review(BaseModel):

  def __init__(self):
    self.place_id = ""
    self.user_id = ""
    self.text = ""
    super().__init__()
