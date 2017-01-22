PostCode UK
===========

A small library for validating and formatting UK postcodes


[![Build Status](https://travis-ci.org/josecolella/postcode_uk.svg?branch=master)](https://travis-ci.org/josecolella/postcode_uk)

The library uses no-external dependencies, and only uses the built-in `re` module.
The regex to format and validate the UK post code is the following:

`^(?P<outwardcode>(?P<postarea>[a-zA-Z]{1,2})(?P<postdistrict>[0-9]{1,2}[a-zA-Z]?))(?P<inwardcode>(?P<postsector>\s[0-9])(?P<postunit>[a-zA-Z]{2}))$`

The regex matches the description of valid UK postcodes that is found ![Here](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting)


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

