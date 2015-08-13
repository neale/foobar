from operator import itemgetter

def answer(meetings):
    # sort meetings by start time
    meetings.sort(key = itemgetter(1))

    # list of all possible schedules
    schedules = []

    # initialize with first meeting
    schedules.append([meetings[0]])

    # set maximum with initialization schedule
    maximum = len(schedules[0])

    # try each starting point
    for i in xrange(len(meetings)):
        for schedule in schedules:
           # if end time is greater than last start time...
           if meetings[i][0] >= schedule[-1][1]:
               # ... append to the schedule and set the new max
               schedule.append(meetings[i])
               maximum = max(len(schedule), maximum)

        schedules.append([meetings[i]])

    return maximum
