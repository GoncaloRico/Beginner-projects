'''There's some unrest in the minion ranks: minions with ID numbers like. "1", "42", and other "good" numbers have been lording it over the poor-minions who are stuck with more boring. IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random. IDs based on a Completely Foolproof Scheme. Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new. ID number will be the next five digits in  the string. So if a minion draws "3" their ID number will be "71113". Help the Commander assign  these IDs. by writing a function solution (n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000. 
'''
#1- Function to find all prime numbers from 0 to 100 #DONE
#2- Get a single long string with all prime numbers #DONE
#3- Function to draw a random number that is going to be the index that will give us our 1st number #DONE
#4- Function to add the next 5 numbers after the chosen index and assign it to a minion 
#5- n is the number of minions and it's between 0 and 10000
import math
import random

n = list(range(1, 5)) #This represents all the minions
numbers = list(range(100))
prime_numbers = []
minion_number = []

def get_prime_numbers():
    for i in numbers:
        if i >= 2:
            square_root = math.isqrt(i) + 1
            l = list(range(2, square_root))
            is_prime = True
            for m in l:
                if i % m == 0: #This checks for divisibility
                    is_prime = False #If it's divisible by any number from 2 to the sqaure root of the number, it is not a prime number.
                    break
            if is_prime:
                prime_numbers.append(i)
    return prime_numbers

get_prime_numbers()

def get_minion_number():
    random_index = random.randint(0, len(prime_numbers) - 1) #Getting a random index
    minion_number.append(prime_numbers[random_index]) #Matching the random index number to the corresponding prime number
    five_subsequent_indexes = random_index
    for i in range(5):
        five_subsequent_indexes += 1
        minion_number.append(five_subsequent_indexes)
    minion_number_as_string = "".join(str(num) for num in minion_number)
    print (minion_number_as_string)

get_minion_number()

prime_numbers_string = "".join(str(num) for num in prime_numbers) #This takes our list of prime numbers and turns them into a string