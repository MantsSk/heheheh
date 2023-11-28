def compare_numbers(numbers):
    # even_sum = sum([num for num in numbers if num % 2 == 0])
    # odd_sum = sum([num for num in numbers if num % 2 != 0])

    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print(even_sum)
    print(odd_sum)
    difference = even_sum - odd_sum

    if difference > 0:
        print("Evens win by: ", difference)
    elif difference < 0:
        print("Odds win by", abs(difference))
    else:
        print("ITS A TIE!!!!!")

numbers_list = [1,2,3,4,5]
numbers_list2 = [1,2,3,4,5,100]


compare_numbers(numbers_list)
compare_numbers(numbers_list2)
