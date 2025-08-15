from task_tracker.logger import get_logger
from task_tracker.models import TaskDTOUser
from task_tracker.tasks import TasksRepo

logger = get_logger(__name__)


def delete_flow_run(repo: TasksRepo, task_id: int) -> None:
    result = repo.delete(task_id)
    logger.debug(f"Deleted: {result}")