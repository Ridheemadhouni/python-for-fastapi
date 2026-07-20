#Create a function that prints all even numbers from 1 to 20.
def even_number():
    i = 1
    while i<=20:
        if i%2==0:
            print(i)
        i += 1
even_number()