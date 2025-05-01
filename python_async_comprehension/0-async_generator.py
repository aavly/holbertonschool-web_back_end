#!/usr/bin/env python3
"""
Task 0. using async_generator to yield values
"""


import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Task 0. using async_generator to yield values
    """
    random_number = random.uniform(0, 10)
    for i in range(10):
        await asyncio.sleep(1)
        yield random_number
