import sys
digits = []
count = 1
sum = 0
maximum = 0
minimum = 0
avg = 0

print("enter a number or enter to finish:")
try:
    data = input()
except ValueError as err:
    print(err)
while data:
    number = int(data)
    digits += [number]
    sum += number
    count += 1
    print("enter a number or enter to finish:")
    data = input()

maximum = max(digits)
minimum = min(digits)


print(f'digits={digits}' ,f'max={maximum}', f'min={minimum}', f'avg={avg}', sep='\n')
