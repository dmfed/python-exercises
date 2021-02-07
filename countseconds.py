import datetime

SEC = 1
MIN = SEC * 60
HOUR = MIN * 60
DAY = HOUR * 24
WEEK = DAY * 7
YEAR = DAY * 365

MEASURES = ((YEAR, "years"), (WEEK, "weeks"), (DAY, "days"), (HOUR, "hours"), (MIN, "minutes"), (SEC, "seconds"))

def count_seconds(sec):
    n = sec
    result = []
    for tup in MEASURES[3:]:
        val = n // tup[0]
        if val > 0:
            result.append(f"{val} {tup[1]}")
            n %= tup[0]
    print(f"{sec} seconds make up", ", ".join(result))

def count_seconds2(sec):
    duration = datetime.timedelta(seconds=sec)
    print(f"{sec} seconds make up", duration)


count_seconds(3600 * 256 * 365 + 3515)
count_seconds2(3600 * 256 * 365 + 3515)
    