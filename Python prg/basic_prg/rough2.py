def outer_function():
    count = 0  # Nonlocal variable

    def inner_function():
        nonlocal count
        count += 1
        print(count)

    inner_function()  # Output: 1
    inner_function() # Output: 2
    print(count)
outer_function()

