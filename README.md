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
EVENT_NAME = "name"
# The ticket type and kktix pages link
EVENT_TICKET = {
    "ticket1-type": "ticket1-link",
    "ticket2-type": "ticket2-link",
}
```
