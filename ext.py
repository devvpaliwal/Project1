def print_pyramid(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(end=" ")

        for j in range(0, i + 1):
            print("*", end=" ")

        print("\r")


rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)
