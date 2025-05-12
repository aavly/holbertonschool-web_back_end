#!/usr/bin/env python3
"""
Change all topics of a school document based on the name
"""


def update_topics(mongo_collecion, name, topics):
    """
    Chance all topics of a school document based on a name
    """
    updated = mongo_collecion.update_many(
        { "name": name }
        { "$set": { "topics": topics } }
    )
    return updated
