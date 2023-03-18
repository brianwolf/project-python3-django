from unittest import mock

from django.test import TestCase
from example import repository, service
from example.classes import Example


class ExampleTest(TestCase):

    @mock.patch.object(repository, "save", return_value=1)
    def test_example_save(self, repository):

        example = Example(
            string='asd',
            integer=12,
            decimal=1.5
        )

        id = service.save(example)

        self.assertEqual(1, id)
