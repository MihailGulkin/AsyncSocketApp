import random


def generate_string(string_length: int = 40) -> str:
    return ''.join(chr(
        [random.randint(65, 90), random.randint(97, 122)]
        [random.randint(0, 1)]
    )
                   for _ in range(string_length))
