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
    r'^(?P<outwardcode>(?P<postarea>[a-zA-Z]{1,2})(?P<postdistrict>[0-9]{1,2}[a-zA-Z]?))(?P<inwardcode>(?P<postsector>\s[0-9])(?P<postunit>[a-zA-Z]{2}))$'
)


def validate(postcode):
    """Returns a boolean if the `postcode` parameter is a valid UK postcode
    Args:
        postcode: a string that represents the UK postcode to validate
    Returns:
        A boolean True if the `postcode` is a valid postcode else returns False
    """
    is_valid = True if re.match(
        UK_POSTCODE_COMPILED_REGEX, postcode
    ) else False
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
    match = re.match(UK_POSTCODE_COMPILED_REGEX, postcode)
    if match:
        formatted_postcode = match.groupdict()

    return formatted_postcode
