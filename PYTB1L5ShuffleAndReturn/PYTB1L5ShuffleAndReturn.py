import random

original = "hallo"
randomised = ''.join(random.sample(original, len(original)))


def randomisedword(randomised):
    return print(str(randomised))

randomisedword(randomised*3)