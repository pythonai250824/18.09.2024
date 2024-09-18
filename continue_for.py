
# print all numbers between range of 1-25 that do not divide by 7
# 1 2 3 4 5 6 8 9 10 11 12 13 15 16 17 18 19 20 22 23 24 25

# 1 if
# 2 if-continue
for i in range(1, 25 + 1):
    if i % 7 == 0:
        continue
    print(i, end = " ")