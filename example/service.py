from example import repository
from example.classes import Example


def list():
    return repository.list()


def get(id: int) -> Example:
    return repository.get(id)


def save(example: Example) -> int:
    return repository.save(example)


def delete(id: int):
    repository.delete(id)
