from task_tracker.logger import get_logger
from task_tracker.models import TaskDTOUser
from task_tracker.tasks import TasksRepo

logger = get_logger(__name__)


def add_flow_run(repo: TasksRepo, description: str) -> None:
    result = TaskDTOUser(description=description)
    result = repo.add(result)
    logger.debug(f"Added: {result}")