#!/usr/bin/python3
def best_score(a_dictionary):
    maxn = 0
    best_k = None
    if len(a_dictionary) == 0:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > maxn:
            maxn = a_dictionary[key]
            best_k = key
    return (best_k)
