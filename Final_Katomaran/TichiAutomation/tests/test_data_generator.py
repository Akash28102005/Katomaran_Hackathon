from utilities.data_generator import DataGenerator


class TestDataGenerator:

    def test_generate_data(self):

        print(DataGenerator.random_first_name())
        print(DataGenerator.random_last_name())
        print(DataGenerator.random_email())
        print(DataGenerator.random_phone())
        print(DataGenerator.random_password())

        assert "@" in DataGenerator.random_email()