def count_digits(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Count the number of digits
    digit_count = 0
    for char in number_str:
        if char.isdigit():
            digit_count += 1
    
    return digit_count

# Test the function
number = 567802
print("Number of digits in", number, ":", count_digits(number))
