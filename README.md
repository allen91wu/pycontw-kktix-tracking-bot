# PyCon TW Ticket Sales Status Tracking Bot

## Description
This bot is developed for PyCon TW staffs to track the sales status of ticket. Bot will fetch the ticket sales status and send the notifications to assigned channel in specific time.
## Commands list

- `!kktix_status`: Show the sales status of kktix page.

## Token
Create a `.env` file.

```
TOKEN='YOUR_TOKEN'
NOTIFY_CHANNEL_ID='CHANNEL_ID'
NOTIFY_TIME='Sunday-14:00'
```

## Event config
Before launching the bot, you can use `event_config.py` to maintain your event information for bot to fetch the data.
```python
# Event name
EVENT_NAME = "PyCon TW 2021"
# The ticket type and kktix pages link for main event
MAIN_EVENT_TICKET = {
    "個人票": "https://pycontw.kktix.cc/events/2021-individual",
    "企業票": "https://pycontw.kktix.cc/events/2021-corporate",
    "保留票": "https://pycontw.kktix.cc/events/2021-reserved",
}
# The target of main event quantity of tickets
MAIN_TICKET_TARGET = "800"
# The ticket type and kktix pages link for child event
CHILD_EVENT_TICKET = {
    "Sprint": "https://pycontw.kktix.cc/events/20210926-sprints",
}
```
