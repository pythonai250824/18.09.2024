
num: int = 0
counter: int = 0
while num % 7 == 0:
    num = int(input('enter number: '))
    counter += 1
    if num % 11 == 0:
        break
else:
    print(f"you gave {counter - 1} numbers divide by 7")

print('goodbye')
