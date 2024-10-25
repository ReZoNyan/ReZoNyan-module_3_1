count = 0


# Функция подсчета
def count_calls():
    global count
    count += 1
    return count


#
def string_info(name):
    name = str(name)
    len_string = len(name)
    upper_string = name.upper()
    lower_string = name.lower()
    my_tuple = (len_string, upper_string, lower_string)
    count_calls()
    return my_tuple


def is_contains(new_string, new_list):
    new_string = str(new_string)
    new_string.lower()
    len_list = len(new_list)
    count_calls()
    a = 0
    for i in range(len_list):
        new_list[i] = new_list[i].lower()
        if new_list[i] == new_string:
            a = True
            break
        else:
            a = False
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('urban', ['String', 'UPPER', 'lower', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic', 'lower', 'urBAN']))

print(count)
