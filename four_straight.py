import random
import secrets
import numpy.random as np_random

# Estimate the probability of rolling a straight

dice = 3
trials = 100000
good = 0
not_in = 0
one = 0
not_one = 0
one_not_two = 0
not_two = 0
for x in range(trials):
    rolls = random.choices([1, 2, 3, 4, 5, 6], k=dice)
    if (1 in rolls) and (2 in rolls):
        good += 1

    if (1 not in rolls) and (2 not in rolls):
        not_in += 1

    if 1 in rolls:
        one += 1

    if 1 not in rolls:
        not_one += 1

    if 2 not in rolls:
        not_two += 1

    if (1 in rolls) and (2 not in rolls):
        one_not_two += 1


print()
print("probability 1 and 2: ", good/trials)
print()
print("probability not 1 and not 2: ", not_in/trials)
print()
print("probability 1: ", one/trials)
print()
print("probability not 1: ", not_one/trials)
print()
print()
print("probability 1 and not 2: ", one_not_two/not_two)
print()

# dice = 4
# trials = 100000
# kind = 3
# good = 0
# for x in range(trials):
#     rolls = [random.randint(1, 6) for y in range(dice)]
#     rolls.sort()

#     cnt = 1
#     for y in range(1, len(rolls)):
#         diff = (rolls[y] - rolls[y-1])
#         if diff == 0:
#             cnt += 1
#         else:
#             cnt = 1
#         if cnt == kind:
#             good += 1
#             break

#     #print(rolls)

# print("trials: ", trials)
# print("good: ", good)
# print("probability of "+str(kind)+" kind: ", good/trials)
