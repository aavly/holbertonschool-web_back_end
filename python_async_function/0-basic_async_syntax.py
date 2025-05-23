#!/usr/bin/env python3
"""
Task 0. async coroutine that waits for a random delay and
returns the delay value.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine that waits for the amount of time randomly generated
    then returns that same number once the time has passed
    """
    wait_length = random.uniform(0, max_delay)
    await asyncio.sleep(wait_length)
    return wait_length
