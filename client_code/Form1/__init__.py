from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):

  isLevel1Completed = False
  isLevel2Completed = False
  actualLevel = 1
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_2.visible = False
    self.button_3.visible = False
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    self.actualLevel = 1
    """This method is called when the button is clicked"""
    self.cleartext()
    pass

  def button_2_click(self, **event_args):
    self.actualLevel = 2
    """This method is called when the button is clicked"""
    if self.isLevel1Completed is True:
      self.cleartext()
    else:
      pass

  def button_3_click(self, **event_args):
    self.actualLevel = 3
    """This method is called when the button is clicked"""
    if self.isLevel2Completed is True:
      self.cleartext()
    else:
      pass

  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cleartext()
    if self.actualLevel == 1:
      pass
    elif self.actualLevel == 2:
      pass
    elif self.actualLevel ==3:
      pass
    else:
      pass
  def cleartext(self):
    self.textbox_name = ""
    self.textbox_password = ""