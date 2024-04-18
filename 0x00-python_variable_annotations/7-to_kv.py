#!/usr/bin/env python3

"""
    function return string and square of a number
"""

from typing import Union


def to_kv(K: str, v: Union[int, float]) -> tuple:
    """
        return tuple of K and v
    """
    return (K, v * v)
