import asyncio
from datetime import datetime
import click


async def sleep_for_five():
    await asyncio.sleep(5)


async def sleep_for_three_then_five():
    await asyncio.sleep(3)
    await sleep_for_five()


async def main():
    await asyncio.gather(sleep_for_three_then_five(), sleep_for_five())


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now() - start}", bold=True, bg="white", fg="blue")
