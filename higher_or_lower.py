# def usernum():
#     number = input('Give me a number between 0-10\n')
#
# def random():
#     x = range(0, 11)
#     for r in x:
#         rand = r
import random

def decider():
    number = int(input('Give me a number between 0-10\n'))
    rand = random.randint(0, 11)
    for number > 0 and number <= 10:
        if rand > number:
            print('Too low\nThe random number is ' + str(rand) + '\nYour number is ' + str(number))
        elif number > rand:
            print('Too high\nThe random number is ' + str(rand) + '\nYour number is ' + str(number))
        else:
            print('You got it')


# usernum()
decider()
# print(rand)

# else:
# print("number's not between 1 and 10")
