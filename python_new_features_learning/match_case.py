user_input = int(input("Enter your data : "))

match user_input:
    case num if num > 0:
        print("number is positive")
    case num if num < 0:
        print("number is negative")
    case _:
        print("default case")


user_input = {'Name':'Alkesha'}

match user_input:
    case {'Name' : a}:
        print(f"a : {a}")
    case {'Age' : b}:
        print(f"b : {b}")
    case _:
        print("default case")


