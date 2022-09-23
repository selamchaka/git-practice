def max_value(numbers):
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
