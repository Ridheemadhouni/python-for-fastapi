#Print numbers from 1 to 100, skipping numbers divisible by 3.
i = 1

while i<=100:
    if i%3 == 0:
        i += 1
        continue
    print(i)
    i += 1