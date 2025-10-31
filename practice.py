"""
    CPU bound tasks are not likely to benefit from async, they are split up to a few processes and threads instead.

    I/O bound tasks: HTTP requests, database access, persistent connections, sending emails
    CPU bound tasks: Slow algorithms, parsing, string manipulation

    async shines in tasks that are I/O bound.
    At the heart of asynchronous programming is the event loop. The event loop manages tasks using event queue.
    async/await syntax is used to handle execution over the event loop.

    Blocking functions: Functions that block execution of further code until their execution operation is completed.
    Non-blocking functions: Functions that return immediately, allowing the program to continue execution. They typically use callbacks, futures, or async/await syntax.
"""
import asyncio
from datetime import datetime
import click


# async function can be chained
# async def my_function():
#     ...
#     results = await non_blocking_awaitable()
#     return results
#
# asynd def another_function():
#     results = await my_function()
#     return results

# You can only await something from within an async function and that async function then becomes something you can await.

"""
    Async Python Rules

    1) async Python code does not run itself
        asyncio.run() is used to run async Python.
    2) We can only await from an async function
        Using await without async results in an error.
    3) Awaiting something does not magically make it async
"""

async def sleep_for_five():
    await asyncio.sleep(5)


async def sleep_for_three_then_five():
    await asyncio.sleep(3)
    await sleep_for_five()


async def main():
    # asyncio.gather is used to run multiple coroutines at once
    await asyncio.gather(sleep_for_three_then_five(), sleep_for_five())


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="white", fg="blue")
