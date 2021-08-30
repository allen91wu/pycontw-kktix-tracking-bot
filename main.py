import asyncio
import datetime
import os

import discord  # noqa: F401
import requests
from bs4 import BeautifulSoup
from discord import channel  # noqa: F401
from discord.ext import commands
from dotenv import load_dotenv
from event_config import (
    EVENT_NAME,
    MAIN_EVENT_TICKET,
    CHILD_EVENT_TICKET,
    MAIN_TICKET_TARGET,
)

load_dotenv()
TOKEN = os.getenv("TOKEN")
NOTIFY_CHANNEL_ID = os.getenv("NOTIFY_CHANNEL_ID")
NOTIFY_TIME = os.getenv("NOTIFY_TIME", default="Sunday-14:00")

client = commands.Bot(command_prefix="!")


def kktix_count(display, web):
    r = requests.get(web)
    soup = BeautifulSoup(r.text, "html.parser")
    ticket_count = soup.find("span", class_="info-count")
    if ticket_count:
        if display == "on":
            return ticket_count.text
        if display == "off":
            return int(ticket_count.text.split("/")[0])
    else:
        return "N/A"


def event_ticket_count():
    main_ticket_count = "-------------- **主活動** --------------\n"
    child_ticket_count = "-------------- **子活動** --------------\n"
    main_total = 0

    for ticket in MAIN_EVENT_TICKET.items():
        status_count = kktix_count("off", ticket[1])
        main_total += status_count
        main_ticket_count += f"- {ticket[0]}：{status_count}\n"
    main_ticket_count += f"**總售票人數：{main_total} / {MAIN_TICKET_TARGET}\n**"

    for ticket in CHILD_EVENT_TICKET.items():
        status_count = kktix_count("on", ticket[1])
        child_ticket_count += f"- {ticket[0]}：{status_count}\n"

    return main_ticket_count + child_ticket_count


@client.command()
async def kktix_status(ctx):
    await ctx.message.delete()
    msg = f"**{EVENT_NAME}** 目前售票狀況：\n{event_ticket_count()}"
    await ctx.send(msg)


async def time_task():
    await client.wait_until_ready()
    client.channel = client.get_channel(int(NOTIFY_CHANNEL_ID))
    while not client.is_closed():
        now_time = datetime.datetime.now().strftime("%A-%H:%M")
        if now_time == NOTIFY_TIME:
            msg = f"**{EVENT_NAME}** 本週售票狀況：\n{event_ticket_count()}"
            await client.channel.send(msg)
            await asyncio.sleep(60)
        else:
            await asyncio.sleep(1)
            pass


@client.event
async def on_ready():
    client.loop.create_task(time_task())
    print(f"{client.user} is online")


client.run(TOKEN)
