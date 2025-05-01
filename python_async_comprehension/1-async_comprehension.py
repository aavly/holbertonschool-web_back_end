#!/usr/bin/env python3
"""
Task 1. Coroutine that collects 10 random numbers using
async_generator(), then returns the 10 random numbers
"""


import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Task 1. Coroutine that collects 10 random numbers using
    async_generator(), then returns the 10 random numbers
    """
    numbers = [number async for number in async_generator()]
    return numbers
