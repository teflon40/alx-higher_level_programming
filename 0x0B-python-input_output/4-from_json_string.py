#!/usr/bin/python3
"""Deserialize a JSON string"""
import json


def from_json_string(my_str):
    """
    Deserialize a JSON string
    Args:
        my_str: json string
    Return:
        object
    """
    json.loads(my_str)
