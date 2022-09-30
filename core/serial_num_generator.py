import string
import random

def auto_generate(n):
    numbering = string.digits
    generate = random.sample(numbering, n)
    auto_generate = "".join(generate)
    return auto_generate