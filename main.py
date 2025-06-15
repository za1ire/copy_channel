
from typing import AsyncGenerator
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


async def revers(messages: AsyncGenerator):
    rev_messages = [message async for message in messages]
    return rev_messages[::-1]

async def clone():
    api_hash = ""
    api_id = 0000
    my_channel = 00000 #свой канал
    clone_id = 0000000 #откуда скопировать
    app = Client(name="my_account", api_id=api_id, api_hash=api_hash)
    await app.start()
    messages: AsyncGenerator[Message, None] = app.get_chat_history(chat_id=clone_id)
    reversed_messages = await revers(messages=messages)

    for message in reversed_messages:
        await message.copy(chat_id=my_channel)

if __name__ == "__main__":
    asyncio.run(clone())



