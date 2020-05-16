import hashlib


def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]


def gen_id(string):
    return int(hashlib.md5(str.encode(string)).hexdigest(), 16)


def get_cell(response, keyword, convert=True):
    result = response.xpath('//td[contains(text(), $keyword)]/following-sibling::td/text()', keyword=keyword).extract()
    if keyword in "Can-US Exchange Rate (US ¢)":
        result = result[0]
    else:
        result = result[1]
    if convert == False:
        return result
    else:
        return float(result)
