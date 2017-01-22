import setuptools
from postcode_uk.version import Version


setuptools.setup(name='postcode-uk',
                 version=Version('1.0.0').number,
                 description='A small library to validate and format UK postcodes',
                 long_description=open('README.md').read().strip(),
                 author='Package Author',
                 author_email='josecolella@yahoo.com',
                 url='https://github.com/josecolella/Scurry-Challenge',
                 py_modules=['postcodeuk'],
                 install_requires=[],
                 license='MIT',
                 zip_safe=False,
                 keywords='postcode uk',
                 classifiers=[  # How mature is this project? Common values are
                     #   3 - Alpha
                     #   4 - Beta
                     #   5 - Production/Stable
                     'Development Status :: 3 - Production',

                     # Indicate who your project is intended for
                     'Intended Audience :: Developers',
                     'Topic :: Software Development :: Postcode',

                     # Pick your license as you wish (should match "license"
                     # above)
                     'License :: OSI Approved :: MIT License',

                     # Specify the Python versions you support here. In particular, ensure
                     # that you indicate whether you support Python 2, Python 3
                     # or both.
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.6', ])
