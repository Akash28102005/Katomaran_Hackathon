from utilities.logger import Logger


class TestLogger:

    def test_logger(self):

        log = Logger.get_logger()

        log.info("Browser Opened")

        log.info("Home Page Loaded")

        log.info("Login Successful")

        assert True