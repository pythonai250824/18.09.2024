import random

# for loop which random number between 1-100, 10 times
# print the biggest number and the smallest number

# 5 59 67 32 10 5 99 81 43 61
# max_int 5
# max -- 99
# min -- 5
max_number: int = 1
min_number: int = 100
for _ in range(10):
    # random int
    # check if bigger than max
    rand_int: int = random.randint(1, 100)
    print(rand_int, end=" ")
    if rand_int > max_number:
        max_number = rand_int  # 10
    if rand_int < min_number:
        min_number = rand_int

print()
print(f"maximum number is {max_number}")
print(f"minimum number is {min_number}")


