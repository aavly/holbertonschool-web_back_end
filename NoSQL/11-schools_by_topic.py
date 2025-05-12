#!/usr/bin/env python3
"""
Return list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
