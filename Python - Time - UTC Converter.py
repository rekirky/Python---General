# UTC converter
# Using when patches are released at UTC time
from zoneinfo import ZoneInfo
from datetime import datetime

patch_day = input("Enter patch date (day): ")
patch_time = input("Enter patch start time (24 hour): ")

d = datetime(2021,7,20,14,tzinfo=ZoneInfo("America/Los_Angeles"))
d.astimezone(ZoneInfo('Australia/Brisbane'))

