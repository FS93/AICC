import unittest
from datetime import datetime
from main import checkForLatencyChange

HIGH_LATENCY = 100.0
LOW_LATENCY = 20.0

class TestStringMethods(unittest.TestCase):
    

    def test_high_latency_change_should_return_datetime(self):
        result = checkForLatencyChange(HIGH_LATENCY)
        self.assertIsInstance(result,datetime)

    def test_low_latency_should_return_none(self):
        result = checkForLatencyChange(LOW_LATENCY)
        self.assertIsInstance(result, type(None))
    

