
# 1st way
sum_temp: float = 0.0

for _ in range(1, 5 + 1):
    temperature: float = 0.0
    while True:
        temperature = float(input('temp? '))
        if -50 <= temperature <= 45:
            break
        print("should be between -50 and +45")
    sum_temp += temperature

avg_tmp: float = sum_temp / 5
print(f"average = {avg_tmp}")

# 2nd way
sum_temp: float = 0.0

for _ in range(1, 5 + 1):
    temperature = float(input('temp? '))
    while not -50 <= temperature <= 45:
        print("should be between -50 and +45")
        temperature = float(input('temp? '))
    sum_temp += temperature

avg_tmp: float = sum_temp / 5
print(f"average = {avg_tmp}")