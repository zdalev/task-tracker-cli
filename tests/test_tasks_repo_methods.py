import pytest

from task_tracker.models import TaskDTOJson
from task_tracker.tasks import TasksRepo, StatusEnum


@pytest.fixture
def setup_repo():
    repo = TasksRepo()

    return repo


@pytest.fixture
def setup_dto():
    dto = TaskDTOJson(1,
                  "test_dto",
                  StatusEnum.TODO,
                  "6/26/25",
                  "6/26/25")
    return dto


def test_repo_add_method(setup_repo, setup_dto):
    repo = setup_repo
    dto = setup_dto

    repo.add(dto)

    assert dto.identifier in repo.tasks


def test_repo_update_method(setup_repo, setup_dto):
    repo = setup_repo
    dto = setup_dto

    repo.add(dto)

    repo.update(1, "updated_dto")

    assert repo.tasks.get(dto.identifier).description == "updated_dto"

def test_repo_delete_method(setup_repo, setup_dto):
    repo = setup_repo
    dto = setup_dto

    repo.add(dto)

    repo.delete(dto.identifier)

    assert dto.identifier not in repo.tasks

