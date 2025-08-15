from typing import List

from task_tracker.general import transform_str_to_enum
from task_tracker.logger import get_logger
from task_tracker.tasks import TasksRepo, StatusEnum

logger = get_logger(__name__)


def verify_mark_args(arguments: List) -> tuple:
    _status, _task_id = arguments

    if not _task_id.isdigit():
        raise TypeError

    if not _status:
        raise ValueError

    status = transform_str_to_enum(_status, StatusEnum)

    task_id = int(_task_id)

    return status, task_id


def mark_flow_run(repo: TasksRepo, arguments: list) -> None:
    status, task_id = verify_mark_args(arguments)
    result = repo.mark(status, task_id)
    logger.debug(f"Changed Task Status: {result}")
