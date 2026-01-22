import pytest
from src.cli import validate_args
from unittest.mock import MagicMock

@pytest.mark.parametrize("name,age,expected",[
    (None,-1,False),
    ("Camellia",-1,False),
    (None,18,False),
    ("Camellia",18,True),
])

def test_validate_args(name,age,expected):
    args=MagicMock()
    args.name=name
    args.age=age
    assert validate_args(args) == expected

