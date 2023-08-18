#This is going to be a randomnly picked madlib with user input.
from Madlibs_samples import programming, hp, hunger
import random

if __name__ == '__main__':
    x = random.choice([programming, hp, hunger])
    x.madlib()

