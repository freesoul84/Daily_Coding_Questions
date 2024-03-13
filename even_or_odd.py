
# To check if the given number is even  or odd
# n & 1 == 0 then number is even
# n & 1 == 1 then number is odd
def even_or_odd(number):
    if number & 1 == 0:
        return f"Number {number} is odd number"
    else:
        return f"Number {number} is even number"

number = int(input("enter number : "))
print(even_or_odd(number))
