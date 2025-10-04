from task_tracker.general import transform_str_to_enum
from task_tracker.logger import get_logger
from task_tracker.tasks import TasksRepo, StatusEnum

logger = get_logger(__name__)


def list_flow_run(repo: TasksRepo, status: str) -> None:
    status = transform_str_to_enum(status, StatusEnum)
    result = repo.get_by(status, "status")
    logger.debug(f"Listed: {result}")

