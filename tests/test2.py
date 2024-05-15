#!usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def test_id_should_be_unique_for_each_instance(self):
        instance1 = BaseModel()
        instance2 = BaseModel()

        self.assertNotEqual(instance1.id, instance2.id)

        instances = [BaseModel() for _ in range(10)]

        unique_ids = set(instance.id for instance in instances)
        self.assertEqual(len(instances), len(unique_ids))

        for instance in instances:
            self.assertNotEqual(instance.id, "")

    def test_id_should_be_a_string(self):
        instance = BaseModel()

        self.assertIsInstance(instance.id, str)

    def test_created_at_should_be_datetime(self):
        instance = BaseModel()

        self.assertIsInstance(instance.created_at, datetime.datetime)

    def test_updated_at_should_be_datetime(self):
        instance = BaseModel()

        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        instance = BaseModel()
        initial_updated_at = instance.updated_at

        instance.save()

        self.assertGreater(instance.updated_at, initial_updated_at)


if __name__ == '__main__':
    unittest.main()
