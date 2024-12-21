def draw_pattern():
    # Get the size of the pattern
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")  # Print asterisks as required by the check
        print()  # Move to the next line after printing all asterisks in the row
        row += 1

if __name__ == "__main__":
    draw_pattern()
