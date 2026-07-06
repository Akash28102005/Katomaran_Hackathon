from testdata.credentials import *


class TestCredentials:

    def test_credentials_loaded(self):

        assert VALID_EMAIL != ""
        assert INVALID_EMAIL != ""
        assert FIRST_NAME != ""