'''
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3
import bcrypt
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
conn = sqlite3.connect(data_files['users.db'])
cursor = conn.cursor()

@anvil.server.callable
def level1(username,password):
  query = f"SELECT * from users WHERE username = '{username}'and password = '{password}'"
  result = cursor.execute(query)
  result = cursor.fetchall()
  if result:
    return True, [dict(row) for row in result]
  return False, []
@anvil.server.callable
def level2(username, password):
  query = "SELECT * from users WHERE username = ? and password = ?"
  result = cursor.execute(query,username,password)
  result = cursor.fetchall()
  if result:
    return True, [dict(row) for row in result]
  return False, []
@anvil.server.callable
def level3(username,password):
  query = "SELECT password, username FROM users WHERE username = ?"
  result = cursor.execute(query,username)
  result = cursor.fetchone()
  if result:
    hashed_pw = result["password"]
        
    if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
        return True, {"username": result["username"]}
    return False, []
'''
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3
import bcrypt

# Connect to the database
conn = sqlite3.connect(data_files['users.db'])
conn.row_factory = sqlite3.Row  # Enables access to rows as dictionaries
cursor = conn.cursor()

@anvil.server.callable
def level1(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchall()  # Fetch all matching rows
    if result:
        return True, [dict(row) for row in result]  # Convert rows to dictionaries
    return False, []

@anvil.server.callable
def level2(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))  # Pass parameters as a tuple
    result = cursor.fetchall()
    if result:
        return True, [dict(row) for row in result]
    return False, []

@anvil.server.callable
def level3(username, password):
    query = "SELECT password, username FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()  # Fetch one matching row
    if result:
        hashed_pw = result["password"]
        if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
            return True, {"username": result["username"]}  # Return username if login is successful
    return False, {}
