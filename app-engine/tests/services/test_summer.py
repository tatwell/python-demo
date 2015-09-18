#
# Summer Module Test
#
import unittest
from random import sample, randint

from services.summer import diophantine_subset_sum, SummerTimeoutError


class SummerServiceTest(unittest.TestCase):

    def test_should_find_subset_for_set_with_five_positive_integers(self):
        number_list = [20, 50, 10, 40, 30]
        target = 80
        subset = diophantine_subset_sum(number_list, target)
        self.assertEqual(sum(subset), target)

    def test_should_find_subset_for_sets_with_hundred_or_less_positive_integers(self):
        for size in range(5,100):
            subset_size = randint(1, size)
            number_list = [randint(0, 1000000) for num in range(size)]
            target_subset = sample(number_list, subset_size)
            target = sum(target_subset)

            subset = diophantine_subset_sum(number_list, target)
            self.assertEqual(sum(subset), target, 'Failed for set length: %d' % (size))

    def test_will_fail_for_set_with_negative_integers(self):
        number_list = [-5259, 9625, 5881, 2250, -2951, -2384, -6378, 5556, -2887, 2600]
        target_subset = [-5259, 2250, -2384, -6378]
        target = sum(target_subset)
        self.assertTrue(set(target_subset).issubset(set(number_list)))

        subset = diophantine_subset_sum(number_list, target)
        self.assertNotEqual(sum(subset), target, 'Cannot find subsets for negative values')

    def test_should_raise_timeout_error(self):
        from services import summer
        original_time_limit = summer.TIME_LIMIT
        summer.TIME_LIMIT = 0.05

        number_list = [892850, -628472, 601815, 981126, 587199, -75114, 915490, -89326]
        target = sum([892850, -628472, 601815, 981126, -1])

        with self.assertRaises(SummerTimeoutError):
            diophantine_subset_sum(number_list, target)
            summer.TIME_LIMIT = original_time_limit

