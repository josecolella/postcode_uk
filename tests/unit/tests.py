#!/usr/bin/env python
import os
import sys
import unittest

# Set the correct path to Sudoku module
path = os.path.abspath(os.path.join(
    os.path.dirname('postcodeuk.py'), 'postcodeuk'))
if path not in sys.path:
    sys.path.insert(0, path)
import postcodeuk


class TestPostCode(unittest.TestCase):

    def setUp(self):
        self.valid_postcode_parameters = set((
            "outwardcode", "postarea", "postdistrict",
            "inwardcode", "postsector", "postunit"
        ))

    def test_fails_on_empty_parameter_validate(self):
        with self.assertRaises(Exception):
            postcodeuk.validate()

    def test_fails_on_wrong_input_parameter_type(self):
        with self.assertRaises(TypeError):
            postcodeuk.format(['ST7 4QT'])

    def test_returns_false_on_empty_string_parameter(self):
        is_valid = postcodeuk.validate('')
        self.assertFalse(is_valid)

    def test_returns_empty_dict_on_false_postcode_format(self):
        formatted_postcode = postcodeuk.format('CV5 9FF3')
        self.assertEqual(formatted_postcode, {})

    def test_returns_empty_dict_on_incomplete_postcode_format(self):
        formatted_postcode = postcodeuk.format('CV5 9')
        self.assertEqual(formatted_postcode, {})

    def test_returns_type_dict_format(self):
        formatted_postcode = postcodeuk.format('ST7 4QT')
        self.assertEqual(dict, type(formatted_postcode))

    def test_validation_RG412RD_should_return_true(self):
        candidate = 'RG41 2RD'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_BN150PR_should_return_all_postcode_keys(self):
        candidate = 'BN15 0PR'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_BN59WA_should_return_true(self):
        candidate = 'BN5 9WA'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_BN59WA_should_return_all_postcode_keys(self):
        candidate = 'BN5 9WA'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_UB68TA_should_return_true(self):
        candidate = 'UB6 8TA'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_UB68TA_should_return_all_postcode_keys(self):
        candidate = 'UB6 8TA'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_BL82RS_should_return_true(self):
        candidate = 'BL8 2RS'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_AB423GU_should_return_true(self):
        candidate = 'AB42 3GU'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_UB96TH_should_return_true(self):
        candidate = 'UB9 6TH'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_EC1A1BB_should_return_true(self):
        candidate = 'EC1A 1BB'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_DN551PT_should_return_true(self):
        candidate = 'DN55 1PT'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_EC1Z1BB_should_return_false(self):
        candidate = 'EC1Z 1BB'
        self.assertFalse(postcodeuk.validate(candidate))

    def test_formatting_UB96TH_should_return_all_postcode_keys(self):
        candidate = 'UB9 6TH'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_ZE10TH_should_return_true(self):
        candidate = 'ZE1 0TH'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_ZE10TH_should_return_all_postcode_keys(self):
        candidate = 'ZE1 0TH'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_ZE10QX_should_return_true(self):
        candidate = 'ZE1 0QX'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_ZE10QX_should_return_all_postcode_keys(self):
        candidate = 'ZE1 0QX'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_BH52AF_should_return_true(self):
        candidate = 'BH5 2AF'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_formatting_LE113PW_should_return_all_postcode_keys(self):
        candidate = 'LE11 3PW'
        formatted_postcode = postcodeuk.format(candidate)
        for key in formatted_postcode.keys():
            self.assertIn(key, self.valid_postcode_parameters)

    def test_validation_QA19AA_should_return_false(self):
        candidate = 'QA1 9AA'
        self.assertFalse(postcodeuk.validate(candidate))

    def test_validation_AB5O9AA_should_return_false(self):
        candidate = 'AB5O 9AA'
        self.assertFalse(postcodeuk.validate(candidate))

    def test_validation_WC1A9AA_should_return_true(self):
        candidate = 'WC1A 9AA'
        self.assertTrue(postcodeuk.validate(candidate))

    def test_validation_BL01BB_should_return_true(self):
        candidate = 'BL0 1BB'
        self.assertTrue(postcodeuk.validate(candidate))


if __name__ == '__main__':
    unittest.main()
