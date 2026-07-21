import datetime
import unittest

from src.clock import Clock


class TestClock(unittest.TestCase):

    def test_get_date_returns_datetime(self):
        clock = Clock()
        result = clock.get_date()
        self.assertIsInstance(result, datetime.datetime)

    def test_get_date_returns_current_time(self):
        clock = Clock()
        before = datetime.datetime.now()
        result = clock.get_date()
        after = datetime.datetime.now()
        self.assertGreaterEqual(result, before)
        self.assertLessEqual(result, after)
