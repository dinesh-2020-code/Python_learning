# panagram = "The quick brown fox jumps over the lazy dog\n\
# ok"

# words = panagram.split() # if we are not providing any argument to split() method, then it will
#                         # split on basis of whitespace char (spaces, tabs or newline chars)
# print(words)
# numbers = "111,223,456,564,5442,45"
# print(numbers.split(","))


numbers = "9,223;372:036 854,775;807"
separators = numbers[1::4] # ",;: ,;"
generated_list = [char if char not in separators else " " for char in numbers]
print(generated_list)
# values = ("".join(char if char not in separators else " " for char in numbers)).split()
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)
# print(type(values_list[0]))
values_list = [int(item) for item in values_list]
print(values_list)
# print(type(values_list[0]))