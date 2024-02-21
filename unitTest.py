# from unittest import TestCase


# class TestFilter(TestCase):
#     def test_always_pass(self):
#         self.assertTrue(True)

from utils.createFilters import *

print(createFilters({"title": "hunger games", "release_year": ["2015", "2018"]}))