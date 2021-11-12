import asyncio
from collections import deque
from re import split

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
    """Animated clocks"""
    if event.fwd_from:
        return
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

@borg.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
    """Animated moons"""
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

@borg.on(events.NewMessage(pattern="\.anim ", outgoing=True))
async def _(event):
    """Animate text, use .anim <text_to_animate> <repeat times (optional)>"""
    if event.fwd_from:
        return
    try:
        to_anim = split(" ", event.text)[1]
    except IndexError:
        await event.edit("Не указан текст для анимации")
        return
    try:
        repeat_times = int(split(" ", event.text)[2])
    except Exception:
        repeat_times = 4
    deq = deque(list(to_anim))
    for _ in range(len(to_anim) * repeat_times):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
