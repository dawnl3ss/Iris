import random

def gen_unique_port() -> int :
    return random.randint(11111, 65535)