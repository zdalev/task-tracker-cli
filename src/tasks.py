import dataclasses
import enum


class StatusEnum(enum.Enum):
    TODO = enum.auto()
    INPROGRESS = enum.auto()
    DONE = enum.auto()


@dataclasses.dataclass
class TaskDTO:
    identifier: int
    description: str
    status: StatusEnum
    createdAt: str
    updatedAt: str


class TasksRepo:
    def __init__(self):
        self.tasks = []

    def add(self, task: TaskDTO):
        pass

    def update(self, task_id: int, value: str):
        pass

    def delete(self, task_id: int):
        pass
