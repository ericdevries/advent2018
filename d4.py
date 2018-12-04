from collections import namedtuple
import re
import numpy
import datetime
from operator import attrgetter
from dataclasses import dataclass

with open('d4input.txt') as f:
    lines = f.readlines()

@dataclass
class Event:
    begins: bool
    sleeps: bool
    wakes: bool
    id: str
    date: datetime.datetime

events = []


for line in lines:
    begins = 'begins shift' in line
    sleeps = 'falls asleep' in line
    wakes = 'wakes up' in line
    guard_id = re.search(r'#(\d+)', line)
    date = re.search(r'\[([0-9\ \-:]+)\]', line)

    if guard_id:
        guard_id = guard_id.group(1)
    
    if date:
        date = datetime.datetime.strptime(date.group(1), '%Y-%m-%d %H:%M')

    event = Event(begins=begins, sleeps=sleeps, wakes=wakes, id=guard_id, date=date)
    events.append(event)

events = sorted(events, key=attrgetter('date'))
merged = []
guard_id = None

for event in events:
    if event.id:
        guard_id = event.id

    event.id = guard_id

for event in events:
    print(event)

def get_minutes_asleep(guard_id, data):
    guard_data = filter(lambda s: s.id == guard_id, data)
    start = None
    total = 0

    for event in guard_data:
        if event.sleeps:
            start = event.date

        if event.wakes:
            minutes = (event.date - start).total_seconds() / 60
            minutes = int(minutes)
            start = None
    
            total += minutes

    return total

def get_most_frequent_minute(guard_id, data):
    guard_data = filter(lambda s: s.id == guard_id, data)
    start = None
    total = numpy.zeros(60)

    for event in guard_data:
        if event.sleeps:
            start = event.date

        if event.wakes:
            minutes = (event.date - start).total_seconds() / 60
            minutes = int(minutes)
            begin = start.minute
            start = None
    
            total[begin:begin+minutes] += 1

    return total

    pass

guard_ids = set(d.id for d in events)
guard_minutes = dict()

for g in guard_ids:
    guard_minutes[g] = get_minutes_asleep(g, events)

sorted_list = sorted(guard_minutes.items(), key=lambda x: x[1])
print('most asleep is %s' % (sorted_list[-1][0]))

result  = get_most_frequent_minute(sorted_list[-1][0], events)

for g in guard_ids:
    res = get_most_frequent_minute(g, events)
    print('guard %s argmax %s - %s' % (g, res.argmax(), res.max()))


import pdb; pdb.set_trace()
