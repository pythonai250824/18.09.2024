"""
   7
[0] 123*
[1] 12***
[2] 1*****
[3] *******

3
[0] 1*
[1] ***

9
[0] 1234*       8
[1] 123***      6
[2] 12*****     4
[3] 1*******    2
[4] *********   0
stars:
1, 3, 5, 7 ...
"""
max_stars: int = 29
stars: int = 1
spaces: int = max_stars // 2

for stars in range(1, max_stars + 2, 2):
    # option 1 using spaces
    #for _ in range(1, spaces + 1):
    # option 2 calculate space for each row
    for _ in range(1, (max_stars - stars) // 2):
        print(' ', end="")
    for _ in range(1, stars + 1):
        print('*', end="")
    print()
    spaces -= 1

# ^ trick
# while stars <= max_stars:
#     print(f"{('*' * stars):^{max_stars}}")
#     stars += 2


