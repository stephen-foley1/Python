
user_input = input("Enter an integer: ")

try:
    number = int(user_input)

    # Check the value of the integer using conditional statements
    if number > 50:
        print("The number is greater than 50")
    elif 30 < number <= 50:
        print("The number is between 30 and 50")
    else:
        print("The number is less than or equal to 30")
except ValueError:
    print("Invalid input. Please enter an integer.")
