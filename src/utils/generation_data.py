import random
import string


class GenerationData:
    """Класс с функциями помощниками"""

    @staticmethod
    def generate_string(length: int) -> str:
        word: str = "".join(
            random.choice(string.ascii_letters) for _ in range(length)
        )
        return word

    @staticmethod
    def generate_email(length: int) -> str:
        name: str = GenerationData.generate_string(length)
        host: str = GenerationData.generate_string(10)
        domain: str = GenerationData.generate_string(5)
        return f"{name}@{host}.{domain}"
