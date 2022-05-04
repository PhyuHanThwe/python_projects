from ast import operator


def calculator(num_1, num_2, op):
    result = 0
    num_1 =int(input("Enter first number: "))
    num_2 = int((input("Enter seconf number: ")))
    op = input("1.+\n2.-\n3.*\nOption : ")
    
    if op == "+":
        result = num_1 + num_2

    elif op == "-":
        result = num_1 - num_2

    elif op == "*":
        result = num_1 * num_2

    else:
        print("Ur operator sign does not correct. Plz check again.")
        exit()
    print(f"{num_1} {op} {num_2} = {result}")

calculator('num_1', 'num_2', 'op')