number = 123321
number_str = str(number)

if len(number_str) == 6:
    first_half = number_str[:3]
    second_half = number_str[3:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    if sum_first_half == sum_second_half:
        print("Упс....СЧАСТЛИВЫЙ БИЛЕЕЕЕТ!")
    else:
        print('Ого! не тот билет!')
else:
    print(f"Похоже билет не тот, такое дело - там должно быть 6 чисел, а ты пихнул мне len(number_str)")
