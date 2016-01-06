"""
Test module for the Fedex Config Object.
"""

import unittest

import sys

sys.path.insert(0, '..')
from fedex.config import FedexConfig




class FedexConfigObjectTests(unittest.TestCase):
    """
    These tests verify that the fedex config object is working properly.
    """

    def test_fedex_config(self):
        # Need to pass at least key and password
        with self.assertRaises(TypeError):
            FedexConfig()

        # Test minimum set of credentials, key and password
        config = FedexConfig('key', 'password')
        assert config.key
        assert config.password

        # Test with all parameters, including overwrite wsdl path
        config = FedexConfig(key='', password='', account_number=None, meter_number=None,
                             freight_account_number=None,
                             integrator_id=None, wsdl_path='/wsdls',
                             express_region_code=None, use_test_server=False)

        assert config.wsdl_path

if __name__ == "__main__":
    unittest.main()
