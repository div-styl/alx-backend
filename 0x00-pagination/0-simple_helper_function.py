#!/usr/bin/env python3
"""func returns index and an end of the range"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """returns index and an end of the range"""
    return ((page - 1) * page_size, page * page_size)
