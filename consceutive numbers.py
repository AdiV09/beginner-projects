def consecutive_numbers_sum(start_range, end_range, even):
    number_sum = 0
    for i in range(start_range, end_range + 1):
        if even:
            if i % 2 == 0:
                number_sum += i

        else:
            if i % 2 != 0:
                pass

    return number_sum


def consecutive_even_numbers_sum(numbers):
    return numbers * (numbers + 1)


def consecutive_odd_numbers_sum(numbers):
    return numbers * numbers


print(consecutive_odd_numbers_sum(5))
