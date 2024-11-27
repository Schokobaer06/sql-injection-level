from ._anvil_designer import Level1Template
from anvil import *


class Level1(Level1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
