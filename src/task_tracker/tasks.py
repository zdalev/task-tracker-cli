import enum
import typing

from general import get_current_date


class StatusEnum(enum.Enum):
    TODO = enum.auto()
    INPROGRESS = enum.auto()
    DONE = enum.auto()


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
        if task.identifier:
            self.tasks[task.identifier] = task
            return

    def update(self, task_id: int, value: str):
        task = self.tasks.get(task_id)
        task.description = value
        task.updatedAt = get_current_date()

    def delete(self, task_id: int):
        self.tasks.pop(task_id)
