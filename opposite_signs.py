# Check if given numbers number1 and number2 has opposite signs
# number1 and number2 has opposite signs if number1 XOR number2 < 0 else it has same signs.
# negative numbers have 1 to their leftmost bit. so if both numbers are negative then its output will be 0 to leftmost bit which indicates positive number.
# else if one number has negative sign and other number has positive sign which indicates the XOR operation output has leftmost bit 1 which indicates both number has different signs
number1 = int(input())
number2 = int(input())

def opposite_numbers(number1, number2):
    if number1 ^ number2 < 0:
        return "Numbers have opposite signs"
    else:
        return "Numbers have same signs"
    
print(opposite_numbers(number1, number2))
