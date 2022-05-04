def is_triangle(size_1, size_2, size_3):
    size_1 = input("Enter size_1: ")
    size_2 = input("Enter size_2: ")
    size_3 = input("Enter size_3: ")

    if all([size_1 + size_2 > size_3, size_2 + size_3 > size_1, size_1 + size_3 > size_2]):
        return print("This is a triangle.")
    return print("This is not a triangle.")

print(is_triangle('size_1', 'size_2', 'size_3'))