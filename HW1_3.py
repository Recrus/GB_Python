number = 0
while True:
    number = str(input("Write your lucky number\n"))
    if len(number) == 6:
        break

firstThreeDigits = number[:3]
secondThreeDigits = number[3:6]
firstSum = 0
secondSum = 0

for digit in firstThreeDigits:
    firstSum += int(digit)

for digit in secondThreeDigits:
    secondSum += int(digit)

if firstSum == secondSum:
    print("Lucky!")
else:
    print("No lucky for you today((")
