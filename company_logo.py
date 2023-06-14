#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    s = input()
    word_dict = dict()
    for i in range(len(s)):
        if s[i] in word_dict:
            word_dict[s[i]] += 1
        else:
            word_dict[s[i]] = 1
    # sort by value descending
    sorted_keys = sorted(word_dict.keys(), key=lambda x: word_dict[x], reverse=True)

    for i in range(3):
        print(f"{sorted_keys[i]} {word_dict[sorted_keys[i]]}")
