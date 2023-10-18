rows = int(input("Input how many rows: "))
columns = int(input("Input how many columns: "))
symbol = input("Input symbol that you want to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()