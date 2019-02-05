from unittest import TestCase
from parameterized import parameterized
from .. import cangaroos_jumps


class TestKangaroo(TestCase):

    @parameterized.expand([
        [(4, 7, 4, 0), True, 'Equal starting positions'],
        [(4, 7, 5, 7), False, 'Equal speeds'],
        [(-1, -9, -5, -7), True, 'Negative speeds, first kangaroo is on the right'],
    ])
    def testParameterized(self, args, expected_result, name):
        actual_result = cangaroos_jumps.kangaroo(*args)
        self.assertEqual(actual_result, expected_result, msg=name)

    def testEqualStartingPositions(self):
        x1, v1, x2, v2 = 4, 7, 4, 0
        actual_result = cangaroos_jumps.kangaroo(x1, v1, x2, v2)
        self.assertTrue(actual_result)

    def testEqualSpeedsReturnsFalse(self):
        x1, v1, x2, v2 = 4, 7, 5, 7
        actual_result = cangaroos_jumps.kangaroo(x1, v1, x2, v2)
        expected_result = False
        self.assertEqual(actual_result, expected_result)
