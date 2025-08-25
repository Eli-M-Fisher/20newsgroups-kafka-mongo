"""
Here I handle loading (and also sampling) data from a 20newsgroups dataset.
"""
from sklearn.datasets import fetch_20newsgroups
import random

INTERESTING = []

NOT_INTERESTING = []

def load_messages():
    """
    Here I loaded messages from the dataset.
    
    and then a list of tuples (subject, text) is returned
    """
    return messages