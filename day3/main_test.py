import unittest

from day3.main import split_rucksack, get_rucksack_duplicate_item, get_priority, get_rucksack_priority, \
    get_priority_sum_for_rucksacks, get_rucksacks_duplicate_item, get_priority_sum_for_groups


class MainTestCase(unittest.TestCase):

    def test_split_rucksack_returns_tuple_with_two_parts(self):

        rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected_result = ("vJrwpWtwJgWr", "hcsFMMfFFhFp")

        result = split_rucksack(rucksack)

        self.assertEqual(expected_result, result)

    def test_get_rucksack_duplicate_item_returns_duplicate_item(self):

        rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected_result = "p"

        result = get_rucksack_duplicate_item(rucksack)

        self.assertEqual(expected_result, result)

    def test_get_rucksacks_duplicate_item_returns_duplicate_item(self):

        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        ]
        expected_result = "r"

        result = get_rucksacks_duplicate_item(rucksacks)

        self.assertEqual(expected_result, result)

    def test_get_priority_with_lowercase_item_returns_correct_value(self):

        item = "a"
        expected_result = 1

        result = get_priority(item)

        self.assertEqual(expected_result, result)

    def test_get_priority_with_uppercase_item_returns_correct_value(self):

        item = "A"
        expected_result = 27

        result = get_priority(item)

        self.assertEqual(expected_result, result)

    def test_get_rucksack_priority_with_rucksack_containing_item_p_returns_16(self):

        rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected_result = 16

        result = get_rucksack_priority(rucksack)

        self.assertEqual(expected_result, result)

    def test_get_priority_sum_for_rucksacks_with_two_rucksacks_returns_54(self):

        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        ]
        expected_result = 54

        result = get_priority_sum_for_rucksacks(rucksacks)

        self.assertEqual(expected_result, result)

    def test_get_priority_sum_for_groups_returns_18(self):

        group = ["vJrwpWtwJgWrhcsFMMfFFhFp",
                 "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                 "PmmdzqPrVvPwwTWBwg"]
        expected_result = 18

        result = get_priority_sum_for_groups([group, ])

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
