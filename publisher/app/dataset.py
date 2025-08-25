"""
Here I handle loading (and also sampling) data from a 20newsgroups dataset.
"""
from sklearn.datasets import fetch_20newsgroups
import random


INTERESTING = [
    "alt.atheism", "comp.graphics", "comp.os.ms-windows.misc",
    "comp.sys.ibm.pc.hardware", "comp.sys.mac.hardware",
    "comp.windows.x", "misc.forsale", "rec.autos",
    "rec.motorcycles", "rec.sport.baseball"
]

NOT_INTERESTING = [
    "rec.sport.hockey", "sci.crypt", "sci.electronics",
    "sci.med", "sci.space", "soc.religion.christian",
    "talk.politics.guns", "talk.politics.mideast",
    "talk.politics.misc", "talk.religion.misc"
]

def load_messages():
    """
    Here I loaded messages from the dataset.
    
    and then a list of tuples (subject, text) is returned
    """
    interesting_data = fetch_20newsgroups(subset="all", categories=INTERESTING)
    not_interesting_data = fetch_20newsgroups(subset="all", categories=NOT_INTERESTING)

    messages = []
    for _ in range(n):
        messages.append(("interesting", random.choice(interesting_data.data)))
        messages.append(("not_interesting", random.choice(not_interesting_data.data)))

    return messages