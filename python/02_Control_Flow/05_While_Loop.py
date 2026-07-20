#Find the sum of numbers from 1 to n
num = int(input("Enter a number: "))

total_sum = 0
i = 1

while i<=num:
    total_sum += i
    i += 1
print("The sum of number from 1 to",num,":",total_sum)