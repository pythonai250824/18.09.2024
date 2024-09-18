
"""
[1]1       1..1
[2]12      1..2
[3]123     1..3
[4]1234    1..4
[5]12345   1..5
[4]1234    1..4
[3]123     1..3
[2]12      1..2
[1]1       1..1
"""
number: int = int(input('what is the triangle size (must be positive)? '))
for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print()
for row in range(number - 1, 0, -1):
    for col in range(1, row + 1):
        print(col, end="")
    print()