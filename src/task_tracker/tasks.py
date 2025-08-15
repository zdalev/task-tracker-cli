import enum
import logging
import typing

from task_tracker.general import get_current_date

logger = logging.getLogger(__name__)


class StatusEnum(enum.Enum):
    INPROGRESS = "in-progress"
    DONE = "done"
    TODO = "todo"


class TaskInterface(typing.Protocol):
    identifier: int
    description: str
    status: StatusEnum
    createdAt: str
    updatedAt: str


class TasksRepo:
    def __init__(self, tasks: typing.Dict[int, TaskInterface] = None):
        self.tasks = tasks if tasks else {}

    def add(self, task: TaskInterface):
        try:
            _task_id = max(self.tasks.keys())
            task_id = _task_id + 1
        except ValueError as e:
            logger.debug(f"Exception: {e}; Setting ID to 1.")
            task_id = 1
        task.identifier = task_id
        self.tasks.update({task_id:task})
        current_date = get_current_date()
        task.createdAt = current_date
        task.updatedAt = current_date

        return task

    def update(self, task_id: int, value: str):
        task = self.tasks.get(task_id)
        task.description = value
        task.updatedAt = get_current_date()

        return task

    def delete(self, task_id: int):
        result = self.tasks.pop(task_id)

        return result

    def mark(self, status, task_id):
        task = self.tasks.get(task_id)
        task.status = status
        task.updatedAt = get_current_date()

        return task

