import time
from datetime import datetime, timedelta

def bin_colour(colour):
    fortnight = 14
    if(colour == "blue"):
        StartDate = datetime(2017, 10, 26)
    elif (colour == "grey"):
        StartDate = datetime(2017, 11, 2)
    CurrentDate = datetime.now()
    Thursday1 = (StartDate - timedelta(days=StartDate.weekday()))
    Thursday2 = (CurrentDate - timedelta(days=CurrentDate.weekday()))
    weeks = ((Thursday2 - Thursday1).days / fortnight)

    print("Start Date {}".format(StartDate))

    next_pickup = (StartDate + timedelta(days=(weeks * 14)))
    for each in range(int(weeks)):
        bin_pickups = StartDate + timedelta(days=fortnight)
        fortnight += 14
        print("Bin pickups: {}".format(bin_pickups))
print(bin_colour("grey"))



