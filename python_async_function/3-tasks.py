#!/usr/bin/env python3
"""
Task 3. Regular function that takes an integer max_delay
and returns an asyncio.Task
"""


import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Task 2. takes an integer and returns an asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
