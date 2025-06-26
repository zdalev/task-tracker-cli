import dataclasses

from src.tasks import StatusEnum


@dataclasses.dataclass
class TaskDTOJson:
    identifier: int
    description: str
    status: StatusEnum
    createdAt: str
    updatedAt: str


@dataclasses.dataclass
class TaskDTOUser:
    identifier: int = dataclasses.field(init=False)
    description: str
    status: StatusEnum = dataclasses.field(default=StatusEnum.TODO)
    createdAt: str = dataclasses.field(init=False)
    updatedAt: str = dataclasses.field(init=False)
