from datetime import datetime

from example.classes import Example


def example_to_json(e: Example) -> dict[str, object]:
    return {
        'string': e.string,
        'integer': e.integer,
        'decimal': e.decimal,
        'id': e.id,
        'date': e.date.isoformat(),
    }


def json_to_example(d: dict[str, object]) -> Example:
    return Example(
        string=d['string'],
        integer=d['integer'],
        decimal=d['decimal'],
        id=d.get(id, None),
        date=datetime.fromisoformat(d['date']),
    )
