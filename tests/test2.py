import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_should_be_unique_for_each_instance(self):
        # Create two instances of BaseModel
        instance1 = BaseModel()
        instance2 = BaseModel()

        # Check if the IDs are unique
        self.assertNotEqual(instance1.id, instance2.id)

        # Create a list of multiple instances
        instances = [BaseModel() for _ in range(10)]

        # Check if all IDs in the list are unique
        unique_ids = set(instance.id for instance in instances)
        self.assertEqual(len(instances), len(unique_ids))

        # Check if the IDs are not empty
        for instance in instances:
            self.assertNotEqual(instance.id, "")

    def test_id_should_be_a_string(self):
        # Create an instance of BaseModel
        instance = BaseModel()

        # Check if the ID is a string
        self.assertIsInstance(instance.id, str)

    def test_created_at_should_be_datetime(self):
        # Create an instance of BaseModel
        instance = BaseModel()

        # Check if the created_at attribute is a datetime object
        self.assertIsInstance(instance.created_at, datetime.datetime)

    def test_updated_at_should_be_datetime(self):
        # Create an instance of BaseModel
        instance = BaseModel()

        # Check if the updated_at attribute is a datetime object
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        # Create an instance of BaseModel
        instance = BaseModel()
        initial_updated_at = instance.updated_at

        # Call the save method
        instance.save()

        # Check if the updated_at attribute has been updated
        self.assertGreater(instance.updated_at, initial_updated_at)

if __name__ == '__main__':
    unittest.main()
