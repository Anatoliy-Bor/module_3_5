
def get_multiplied_digits(namber):
    str_number = str(namber)
    first = int(str_number[:1])
    for i in str_number:
        if len(str_number) > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first

result = get_multiplied_digits(40203)
print(result)