"""
Module handling useful functions across cogs


Views:
    ProgressView:           Creates a View with three buttons, one to increase the clock by one, one to decrease it by one, and one to delete it

Database:
    generate_random_id      Generates a random id for a view

"""
from .views import ProgressView
from .database import generate_random_id



__all__ = [
    "ProgressView"

    "generate_random_id"    
]