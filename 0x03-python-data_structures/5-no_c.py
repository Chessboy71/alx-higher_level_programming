#!/usr/bin/python3
def no_c(my_string):
    while (my_string.find('c') != -1):
        my_string = my_string[:my_string.find(
            "c")] + my_string[my_string.find('c')+1:]
    while (my_string.find('C') != -1):
        my_string = my_string[:my_string.find(
            "C")] + my_string[my_string.find('C')+1:]
    return my_string


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
