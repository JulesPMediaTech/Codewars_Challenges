'''
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
* For seconds = 0, your function should return 
    "now"
    
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
'''


def format_duration(seconds, resp=''):
    if seconds == 0: return 'now'
    while seconds > 0:
        for k, v in {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}.items():
            if seconds >= v:
                n = seconds // v
                resp += f"{n} {k}{'s' if n > 1 else ''}, "
                seconds -= n * v
                break
    return resp if not resp.endswith(', ') else ' and '.join(resp[:-2].rsplit(', ', 1))


secs = 205851834
print(f' duration is: {format_duration(secs)}' )
