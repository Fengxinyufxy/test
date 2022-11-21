# with open('digits.txt') as file:
#     lines = file.readlines()
#
# for line in lines:
#     print (line.rstrip())
#
# string = ''
# for line in lines:
#     string += line.strip()
#
# print (string)
# print (len(string))

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")
#     file_object.write("I love programming.")
#
#
# try:
#     print (5/0)
# except ZeroDivisionError:
#     print ("You can't divide by zero!")

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except IOError:
#     print ("Sorry, the file {} does not exist.".format(filename))

# import json
# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)
# print (numbers)
def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = "{} {} {}".format(first, middle, last)
    else:
        full_name = "{} {}".format(first, last)
        return full_name.title()

