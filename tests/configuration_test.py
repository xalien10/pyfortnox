import unittest

from fortnox import Configuration, ConfigurationError


class ConfigurationTest(unittest.TestCase):
    """
    Test cases for Configuration class
    """

    def setUp(self):
        self.ConfigurationClass = Configuration
        self.valid_options = {
            'base_url': 'https://my.test.base.url',
            'access_token': 'this-is-my-access-token',
            'timeout': 20,
            'client_secret': 'my-test-client-secret'
        }

    def test_config_with_valid_options(self):
        config = self.ConfigurationClass(**self.valid_options)
        self.assertTrue(config.validate())

        valid_option_with_auth_code = {
            'base_url': 'https://my.test.base.url',
            'client_secret': 'my-test-client-secret',
            'authorization_code': 'test-auth-code'
        }
        config = self.ConfigurationClass(**valid_option_with_auth_code)
        self.assertTrue(config.validate())

    def test_invalid_configuration(self):
        invalid_option1 = {
            'base_url': 'fortnox.com',
            'access_token': None,
            'timeout': 20,
            'client_secret': 'my-test-client-secret'
        }
        config = self.ConfigurationClass(**invalid_option1)
        self.assertRaises(ConfigurationError, config.validate)

        invalid_option2 = {
            'base_url': 'fortnox.com',
            'timeout': 20
        }
        config = self.ConfigurationClass(**invalid_option2)
        self.assertRaises(ConfigurationError, config.validate)
