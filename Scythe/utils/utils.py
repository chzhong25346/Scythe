import hashlib


def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]


def gen_id(string):
    return int(hashlib.md5(str.encode(string)).hexdigest(), 16)
