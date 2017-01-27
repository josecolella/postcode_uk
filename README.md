PostCode UK
===========

A small library for validating and formatting UK postcodes


[![Build Status](https://travis-ci.org/josecolella/postcode_uk.svg?branch=master)](https://travis-ci.org/josecolella/postcode_uk)

The library uses no-external dependencies, and only uses the built-in `re` module.
The regex to format and validate the UK post code is the following:

`^(?P<outwardcode>(?P<postarea>[A-PR-UWYZ]{1,2})(?P<postdistrict>[A-HK-Y0-9]{1,2}[A-Z]?))(?P<inwardcode>(?P<postsector>\s[0-9])(?P<postunit>[A-BD-HJLNP-UW-Z]{2}))$`

This is the initial validation regex and afterwards several restriction validations are carried out, such as:
- Areas with only single-digit districts
- Areas with only double-digit districts
- Areas with a district '0'
- Letter validation for third position when outward code followes pattern A9A
- Letter validation for fourth position when outward code AA9A

The regex matches the description of valid UK postcodes that is found [Here](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting)


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
```


##Tests

To test the code run the following commands:

```sh
git clone https://github.com/josecolella/postcode_uk.git
./script/test
```

