import configparser
import datetime
import enum
import json
import pathlib
import typing


class TasksRepo(typing.Protocol):
    tasks: typing.Dict


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

def transform_enum_to_str(member: enum.Enum) -> str:
    return member.value


def write_to_file(repo: TasksRepo) -> None:
    tasks = json.dumps({_id: task.to_json_dict() for _id,task in repo.tasks.items()},indent=4)

    config = configparser.ConfigParser()
    config.read("config.ini")
    tt_file_name = config.get("CONFIG", "TASK_FILE_NAME")

    current_dir = pathlib.Path.cwd()
    tt_path = current_dir / tt_file_name
    tt_path.touch(exist_ok=False)


    tt_path.write_text(tasks)
