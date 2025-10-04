import dataclasses

from task_tracker.general import transform_enum_to_str
from task_tracker.tasks import StatusEnum


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

    def to_json_dict(self)->dict:
        return {
            "identifier": self.identifier,
            "description": self.description,
            "status": transform_enum_to_str(self.status),
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }