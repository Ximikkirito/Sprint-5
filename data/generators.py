import random
import string

def generate_email():
    number = random.randint(100, 999)
    return f"test_testov_13_{number}@yandex.ru"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))