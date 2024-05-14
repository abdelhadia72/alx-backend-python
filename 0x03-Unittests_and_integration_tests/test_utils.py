import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
        
    def test_access_nested_map(self):
        pass