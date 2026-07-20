#Create a function that returns whether a number is even (True) or odd (False)
def number_is_even_or_odd(num):
    if num%2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
answer = number_is_even_or_odd(num)
print(answer)