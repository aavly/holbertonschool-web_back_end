#!/usr/bin/env python3
"""
Insert a new document in a collection
"""


def insert_school(mongo_collecion, **kwargs):
    """
    Insert a new document in a collection based on kwargs
    """
    result = mongo_collecion.insert_one(kwargs)
    return result.inserted_id
