#!/usr/bin/python3
"""Return a JSON-serializable dict description of a class instance."""

def class_to_json(obj):
    """Return the dictionary description of a class instance.

    The returned dict contains the instance attributes only (obj.__dict__),
    which the task guarantees are already JSON-serializable types.
    """
    #Every python obj has a attribute __dict__
    return obj.__dict__
