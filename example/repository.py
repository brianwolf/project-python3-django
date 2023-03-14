from core.exception import AppException
from example.classes import Example
from example.error import ExampleError
from example.models import ExampleEntity


def list() -> list[int]:
    search = ExampleEntity.objects.all()

    if search.exists():
        return [e.id for e in search]
    return []


def get(id: int) -> Example:
    search = ExampleEntity.objects.filter(id=id)

    if search.exists():
        return search.get().to_class()
    return None


def save(example: Example) -> int:
    entity = ExampleEntity.from_class(example)
    entity.save()
    return entity.id


def delete(id: int):
    search = ExampleEntity.objects.filter(id=id)

    if not search.exists():
        msj = f'Example with id {id} not exist'
        raise AppException(ExampleError.EXAMPLE_OBJECT_NOT_EXIST, msj)
    search.delete()
