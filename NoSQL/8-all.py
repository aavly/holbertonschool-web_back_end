#!/usr/bin/env python3
"""
List all documents in a collection
"""


def list_all(mongo_collecion):
    """
    Listing all documents in a passed collection
    """
    return list(mongo_collecion.find())
