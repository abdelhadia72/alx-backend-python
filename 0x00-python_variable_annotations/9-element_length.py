#!/usr/bin/env python3

"""
    Let's duck type an iterable object
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        return a list of tuples
    """
    return [(i, len(i)) for i in lst]
