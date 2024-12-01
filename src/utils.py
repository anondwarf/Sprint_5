# coding=utf-8
import random
import string


class UtilsForTests:

    @staticmethod
    def generate_random_string(length: int) -> str:
        return "".join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def generate_random_email(length: int) -> str:
        name: str = UtilsForTests.generate_random_string(length)
        domain: str = UtilsForTests.generate_random_string(length)
        zone: str = UtilsForTests.generate_random_string(length)
        return f"{name}@{domain}.{zone}"
