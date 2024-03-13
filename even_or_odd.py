
def even_or_odd(number):
    if number & 1 == 0:
        return "Number {number} is odd number"
    else:
        return "Number {number} is even number"

number = int(input())
print(even_or_odd(number))