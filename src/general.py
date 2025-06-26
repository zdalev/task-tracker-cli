import datetime


def get_current_date():
    _result = datetime.datetime.now()
    result = _result.strftime("%Y-%m-%d %H:%M:%S")
    return result
