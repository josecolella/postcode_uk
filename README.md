PostCode UK
===========

A small library for validating and formatting UK postcodes


[![Build Status](https://travis-ci.org/josecolella/postcode_uk.svg?branch=master)](https://travis-ci.org/josecolella/postcode_uk)

## Usage

```python
import postcodeuk

# Two methods are exposed to the user : validate and format

# Returns true if postcode is a valid UK postcode
is_valid = postcodeuk.validate('ZE1 0QX')

# Returns a dictionary with the UK postcode sections as keys and
# the values as the appropriate part
formatted_postcode = postcodeuk.format('ZE1 0QX')
# Returns
# {
#   'outwardcode': 'ZE1', 'postarea': 'ZE', 'postdistrict': '1',
#   'inwardcode': ' 0QX', 'postsector': ' 0', 'postunit': 'QX'
#  }
