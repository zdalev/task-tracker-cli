import datetime
import enum


def get_current_date():
    _result = datetime.datetime.now()
    result = _result.strftime("%Y-%m-%d %H:%M:%S")
    return result


def transform_str_to_enum(value: str, given_enum: enum.Enum) -> enum.Enum:
    try:
        return given_enum(value)
    except ValueError:
        valid_keys = [e.name for e in given_enum]
        raise ValueError(f"Invalid status: {value}. Must be one of {valid_keys}")
