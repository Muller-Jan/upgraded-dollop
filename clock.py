from telethon import events
import asyncio
from collections import deque
from re import split


@borg.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(events.NewMessage(pattern=r"\.clouds", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("☀️🌤⛅️🌥☁️🌦🌧⛈"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(events.NewMessage(pattern="\.anim ", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	to_anim = split(" ", event.text)[1]
	deq = deque(list(to_anim))
	for _ in range(len(to_anim) * 4):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

