import sqlite3
import uuid

def generate_random_id() -> str:
    """ Generates a random id for a view """
    return str(uuid.uuid4()) # This creates a 128-bit random label, preventing any views from having the same id

