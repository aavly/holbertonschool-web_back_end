#!/usr/bin/env python3
"""
Task 4
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    almost identical to wait_n except task_wait_random
    is being called.
    """
    generated_delays = []
    results_list = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        generated_delays.append(task)
    for each_generated_delay in asyncio.as_completed(generated_delays):
        list_of_delays = await each_generated_delay
        results_list.append(list_of_delays)
    return results_list
