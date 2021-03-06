from setuptools import setup

import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name='mozilla-iam-cis',
    version='0.1.2.1',
    packages=['cis', 'cis/libs', 'cis/plugins', 'cis/plugins/validation'],
    license='MPL 2.0',
    long_description='Mozilla IAM change integration service',
    include_package_data=True,
    test_suite=('setup.test_suite'),
    install_requires=[
        'boto3',
        'everett',
        'watchtower',
        'asn1crypto',
        'cryptography',
        'pluginbase',
        'jsonschema',
        'pykmssig',
        'moto'
    ]
)
