from django.db import models
from django.utils import timezone

from example.classes import Example


class ExampleEntity(models.Model):
    id = models.AutoField(primary_key=True)
    string = models.CharField(max_length=200)
    integer = models.IntegerField()
    decimal = models.DecimalField(decimal_places=5, max_digits=10)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'EXAMPLES'

    def to_class(self):
        return Example(
            id=self.id,
            string=self.string,
            integer=self.integer,
            decimal=self.decimal,
            date=self.date,
        )

    @staticmethod
    def from_class(e: Example) -> 'ExampleEntity':
        return ExampleEntity(
            id=e.id,
            string=e.string,
            integer=e.integer,
            decimal=e.decimal,
            date=e.date,
        )
