#!/usr/bin/env python3
"""
Task 0. using async_generator to yield values
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Task 0. using async_generator to yield values
    """
    random_number = random.uniform(0, 10)
    for i in range(10):
        await asyncio.sleep(1)
        yield random_number
