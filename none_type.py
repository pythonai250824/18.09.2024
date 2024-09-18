
# while loop which inputs number from the user 1-100, until got -999
# print the biggest number and the smallest number
# int float str bool None
max_number: int = None
min_number: int = None
num_count: int = 0

while True:
    num: int = int(input('enter number: '))
    if num == -999:
        break
    if num < 1 or num > 100:
        print('number not in range ...')
        continue
    num_count += 1
    if max_number is None or num > max_number:
        max_number = num  # 10
    if min_number is None or num < min_number:
        min_number = num

print()
print(f"total legit numbers is {num_count}")
print(f"maximum number is {max_number}")
print(f"minimum number is {min_number}")