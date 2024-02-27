import sqlite3
import uuid

def generate_random_id() -> str:
    """ Generates a random id for a view """
    return str(uuid.uuid4()) # This creates a 128-bit random label, preventing any views from having the same id

def get_buttons() -> list[tuple[str]]:
    """ Creates the database if it does not exist, then fetches all data from database """
    # Connects to database
    database_connect = sqlite3.connect("persistent_views.db")
    cursor = database_connect.cursor()
    
    # Creates a table within the database where view_id is unique
    cursor.execute("""CREATE TABLE IF NOT EXISTS buttons(view_id TEXT PRIMARY KEY, segments INTEGER, ticks INTEGER, colour TEXT, title TEXT)""")
    database_connect.commit()

    # Fetches all data as a list of tuples
    cursor.execute("SELECT * FROM buttons") 
    view_parameters = cursor.fetchall()
    if view_parameters == None: return None
    return view_parameters

def save_buttons(id: str, segments: int, ticks: int, colour: str, title: str) -> None:
    """ Saves view parameters in database """
    # Connects to database
    database_connect = sqlite3.connect("persistent_views.db")
    cursor = database_connect.cursor()

    # Adds a row in the database containing the view parameters
    cursor.execute(f"INSERT INTO buttons VALUES (?, ?, ?, ?, ?)", (id, segments, ticks, colour, title))
    database_connect.commit()

def delete_buttons(id: str) -> None:
    """ Deletes button from database using custom id """
    # Connects to database
    database_connect = sqlite3.connect("persistent_views.db")
    cursor = database_connect.cursor()

    # Deletes row with custom id
    cursor.execute("DELETE from buttons WHERE view_id = (?)", (id[:-4],))  # Deletes row with unique id
    database_connect.commit()