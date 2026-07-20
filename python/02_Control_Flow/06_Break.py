#Print numbers from 1 to 100, but stop when you find the first number divisible by both 7 and 9.
i = 0
for i in range(1,101):
    if i%7 == 0 and i%9==0:
        break
    print(i)   