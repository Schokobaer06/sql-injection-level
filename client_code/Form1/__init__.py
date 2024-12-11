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
   #self.button_2.enabled = False
    #self.button_3.enabled = False
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    self.actualLevel = 1
    self.label_actualLevel.text = f"Level {self.actualLevel}"
    """This method is called when the button is clicked"""
    self.cleartext()
    self.clearlabel()
    

  def button_2_click(self, **event_args):
    self.actualLevel = 2
    self.label_actualLevel.text = f"Level {self.actualLevel}"
    """This method is called when the button is clicked"""
    if self.isLevel1Completed is True:
      self.cleartext()
      self.clearlabel()
    else:
      pass

  def button_3_click(self, **event_args):
    self.actualLevel = 3
    self.label_actualLevel.text = f"Level {self.actualLevel}"
    """This method is called when the button is clicked"""
    if self.isLevel2Completed is True:
      self.cleartext()
      self.clearlabel()
    else:
      pass

  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    #self.cleartext()
    if self.actualLevel == 1:
      result, status, query = anvil.server.call('level1',self.textbox_name.text,self.textbox_password.text)
      self.label_status.visible = True
      if status is True:
        self.label_status.text = "Login erfolgreich!"
        self.label_result.visible = True
        self.label_result.text = f"ID: {result[0].get('id')}\nName: {result[0].get('username')}\nPassword: {result[0].get('password')}"
        self.isLevel1Completed = True
        self.button_2.enabled = True
        self.button_1.background = "Green"
        self.button_1.foreground = "White"
        #self.button_2_click()
      else:  
        self.label_status.text = "Login Falsch!"
        self.label_result.visible = False     
      print(result, query, status)

      
      self.cleartext()
    elif self.actualLevel == 2:
      status, result, query = anvil.server.call('level2',self.textbox_name.text,self.textbox_password.text)
      self.label_status.visible = True
      if status is True:
        self.label_status.text = "Login erfolgreich!"
        self.label_result.visible = True
        self.label_result.text = f"ID: {result[0].get('id')}\nName: {result[0].get('username')}\nPassword: {result[0].get('password')}"
        self.isLevel2Completed = True
        self.button_3.enabled = True
        self.button_2.background = "Green"
        self.button_2.foreground = "White"
        #self.button_3_click()
      else:  
        self.label_status.text = "Login Falsch!"
        self.label_result.visible = False     
      print(result)
      print(query)
      self.cleartext()      
    elif self.actualLevel ==3:
      self.cleartext()
    else:
      pass
  def cleartext(self):
    self.textbox_name.text = ""
    self.textbox_password.text = ""
  def clearlabel(self):
    self.label_result.visible = False
    self.label_status.visible = False
    self.label_result.text = ""
    self.label_status.text = ""