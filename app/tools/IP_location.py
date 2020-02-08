import datetime


def d(day=0):
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')

print(f"{d()}<2020-02-08 13:21:32")
