#!/usr/bin/env python3
# -*- coding: utf-8 -*
# Author: Jose Miguel Colella
"""
A small library to validate and format UK postcodes
A UK postcode is made up of the outward code and inward code
Examples of postcodes include "SW1W 0NY", "PO16 7GZ", "GU16 7HF", or "L1 8JQ"

The outward code is the part of the postcode before the single space in
the middle. It is between two and four characters long. Examples of outward
codes include "L1", "W1A", "RH1", "RH10" or "SE1P". A few outward codes are
non-geographic, not divulging where mail is to be sent.

The outward code is made up of the postcode area and postcode district

The inward code is the part of the postcode after the single space in the
middle. It is three characters long. The inward code assists in the delivery
of post within a postal district. Examples of inward codes include "0NY",
"7GZ", "7HF", or "8JQ"

The inward code is made up of the postcode sector and postcode unit
"""
import re

UK_POSTCODE_COMPILED_REGEX = re.compile(
    r'^(?P<outwardcode>(?P<postarea>[A-PR-UWYZ]{1,2})(?P<postdistrict>[A-HK-Y0-9]{1,2}[A-Z]?))(?P<inwardcode>(?P<postsector>\s[0-9])(?P<postunit>[A-BD-HJLNP-UW-Z]{2}))$',
    re.IGNORECASE
)

UK_SINGLE_DIGIT_DISTRICT_AREA_VALIDATION = frozenset(('BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS',
                                                      'HX', 'JE', 'LD', 'SM', 'SR', 'WC', 'WN', 'ZE'))
UK_DOUBLE_DIGIT_DISTRICT_AREA_VALIDATION = frozenset(("AB", "LL", "SO"))
UK_AREA_WITH_DISTRICT_ZERO_VALIDATION = frozenset(
    ("BL", "BS", "CM", "CR", "FY", "HA", "PR", "SL", "SS"))

UK_THIRD_LETTER_VALIDATION = 'ABCDEFGHJKPSTUW'
UK_FOURTH_LETTER_VALIDATION = 'ABEHMNPRVWXY'
UK_CENTRAL_LONDON_SPECIAL_AREAS = frozenset(
    ('EC1', 'EC2', 'EC3', 'EC4', 'SW1', 'W1', 'WC1', 'WC3',
     'E1W', 'N1C', 'N1P', 'NW1W', 'SE1P'))


def validate(postcode):
    """Returns a boolean if the `postcode` parameter is a valid UK postcode
    Args:
        postcode: a string that represents the UK postcode to validate
    Returns:
        A boolean True if the `postcode` is a valid postcode else returns False
    """

    is_valid = True
    initial_match = re.match(UK_POSTCODE_COMPILED_REGEX, postcode)
    if initial_match:
        # Passes initial validation
        breakdown_match = initial_match.groupdict()
        postdistrict = breakdown_match['postdistrict']
        postarea = breakdown_match['postarea']
        # Test further restrictions
        validation_dict = {
            'only_double_digit': [postarea in UK_DOUBLE_DIGIT_DISTRICT_AREA_VALIDATION, True if re.match('^[0-9]{2}$', postdistrict) else False],
            'only_single_digit': [postarea in UK_SINGLE_DIGIT_DISTRICT_AREA_VALIDATION, True if re.match('^[0-9]$', postdistrict) else False],
            'zero_district': [True if re.match(r'1?0', postdistrict) else False, postarea in UK_AREA_WITH_DISTRICT_ZERO_VALIDATION],
            'third_position': [True if re.match(r'^[A-PR-UWYZ][0-9][a-z]', breakdown_match['outwardcode'], re.IGNORECASE) else False, postdistrict[-1] in UK_THIRD_LETTER_VALIDATION],
            'fourth_position': [True if re.match(r'[A-PR-UWYZ]{2}[0-9][A-Z]', breakdown_match['outwardcode'], re.IGNORECASE) else False, postdistrict[-1] in UK_FOURTH_LETTER_VALIDATION]
        }
        validation_set = set((False if validation[1] is False and validation[0] else True for validation in validation_dict.values()))

        if False in validation_set:
            is_valid = False
        else:
            is_valid = True
    else:
        is_valid = False
    return is_valid


def format(postcode):
    """Returns a dictionary with all the parameters that make up a UK postcode
    Args:
        postcode: a string that represents the UK postcode to format
    Returns:
        A dictionary with the following keys that represent the sections of a
        UK postcode
            {
                "outwardcode": '...' ,
                "postarea": '...',
                "postdistrict": '...',
                "inwardcode": '...',
                "postsector": '...'
                "postunit": '..'
            }
    """
    formatted_postcode = {}
    if validate(postcode):
        match = re.match(UK_POSTCODE_COMPILED_REGEX, postcode)
        formatted_postcode = match.groupdict()

    return formatted_postcode
