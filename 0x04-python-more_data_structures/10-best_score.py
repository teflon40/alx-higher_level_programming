#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not len(a_dictionary):
        return None
    scores = list(a_dictionary.values())
    max_idx = scores.index(max(scores))
    return list(a_dictionary.keys())[max_idx]
