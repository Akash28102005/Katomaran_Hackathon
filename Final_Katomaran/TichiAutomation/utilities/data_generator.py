import random
import string


class DataGenerator:

    @staticmethod
    def random_first_name():
        names = [
            "Akash",
            "Rahul",
            "Kiran",
            "Arun",
            "Vijay",
            "Rohit"
        ]
        return random.choice(names)

    @staticmethod
    def random_last_name():
        names = [
            "Kumar",
            "Sharma",
            "Singh",
            "Raj",
            "Verma"
        ]
        return random.choice(names)

    @staticmethod
    def random_email():

        random_number = random.randint(100000, 999999)

        return f"test{random_number}@gmail.com"

    @staticmethod
    def random_phone():

        return "9" + "".join(
            random.choices(string.digits, k=9)
        )

    @staticmethod
    def random_password():

        random_string = "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )

        return f"Test@{random_string}"