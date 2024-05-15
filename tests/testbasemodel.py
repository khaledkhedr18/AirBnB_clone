
# Generated by CodiumAI
from models.base_model import BaseModel


import pytest

class TestBaseModel:

    # BaseModel instance is created successfully
    def test_base_model_instance_created_successfully(self):
        base_model = BaseModel()
        assert isinstance(base_model, BaseModel)

    # Creating an instance with arguments
    def test_create_instance_with_arguments(self):
        base_model = BaseModel(arg1='value1', arg2='value2')
        assert isinstance(base_model, BaseModel)