from typing import List

from task_tracker.logger import get_logger
from task_tracker.tasks import TasksRepo

logger = get_logger(__name__)



def verify_update_args(arguments: List) -> tuple:
    _task_id, *_description = arguments

    if not _task_id.isdigit():
        raise TypeError
    if not _description:
        raise ValueError

    description = " ".join(_description)

    task_id = int(_task_id)

    return task_id, description


def update_flow_run(repo: TasksRepo, args: List) -> None:
    try:
        task_id, description = verify_update_args(args)
        result = repo.update(task_id, description)
        logger.debug(f"Updated: {result}")

    except TypeError:
        logger.debug("First passed value is not an numbered ID.")
    except ValueError:
        logger.debug("Missing description.")
