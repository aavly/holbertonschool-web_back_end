#!/usr/bin/env python3
"""
Task 2. executes async_comprehension 4 times 
in parallel using async.gather. returns the total runtime
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Task 2. executes async_comprehension 4 times
    in parallel using async.gather. returns the total runtime
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.perf_counter()
    total_time = end - start
    return total_time
