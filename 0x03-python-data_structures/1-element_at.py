#!/usr/bin/python3
#1-element_at.py

def element_at(my_list, idx):
    """Gets an rlement in s list at given index and retutns it"""
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        return
    return(my_list[idx]
