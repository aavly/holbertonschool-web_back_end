#!/usr/bin/env python3
"""
Task 1. coroutine that spawns wait_random n
times with the specified max delay
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with the specified max delay
    """
    generated_delays = []
    results_list = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        generated_delays.append(task)
    for each_generated_delay in asyncio.as_completed(generated_delays):
        list_of_delays = await each_generated_delay
        results_list.append(list_of_delays)
    return results_list
