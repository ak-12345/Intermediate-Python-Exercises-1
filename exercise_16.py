import numbers


total = 0

for i in range(5):
    while True:
        try:
            num = int(input(f"Enter num {i+1}: "))
            total += num
            break
        except ValueError:
            print("Error, Enter correctly!")
print("Sum: ", total)