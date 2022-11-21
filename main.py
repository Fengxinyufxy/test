# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     print('once"eff"')
#     a = 2**3
#     print(a)
#     tr = [value**3 for value in range(1, 11)]
#     print(tr)
#     message = "the first three items in the list are:"
#     print (message[0:3])
#

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=24)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     full_name = "{} {}".format(first_name, last_name)
#     return full_name
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     first = raw_input("First name: ")
#     if first == 'q':
#         break
#     last = raw_input("last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print ("Hello, {}".format(formatted_name))

# def show_messages(messages):
#     for message in messages:
#         print (message)
#
#
# def send_messages(messages, sent_messages):
#     while messages:
#         sent_message = messages.pop()
#         sent_messages.append(sent_message)
#
#
# messages = ['HELLO!', 'GOOD DAY', 'HAPPY EVERYDAY']
# sent_messages = []
# print ("messages are: ")
# show_messages(messages)
#
# send_messages(messages[:], sent_messages)
# print ("after send message ,the list 'messages' are: ")
# show_messages(messages)
# print ("after send message ,the list 'sent_messages' are: ")
# show_messages(sent_messages)


# def make_pizza(*toppings):
#     print ("Making a pizza with the following toppings:")
#     for topping in toppings:
#         print ("- {}".format(topping))
#
#
# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

# def build_profile (first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

# def make_car(producer, type, **car_info):
#     car_info['producer'] = producer
#     car_info['type'] = type
#     return car_info
#
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def sit(self):
#         print ("{} is now sitting." .format(self.name))
#
#     def roll_over(self):
#             print ("{} rolled over !".format(self.name))
#
#
# mydog = Dog('Willie', 6)
# print ("My dog's name is {}.".format(mydog.name))
# print ("My dog is {} years old.".format(mydog.age))
# mydog.sit()
# mydog.roll_over()


class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.oldmeter_reading =0

    def get_descriptive_name(self):
        long_name = "{} {} {}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_oldmeter(self):
        print ("This car has {} miles on it.".format(self.oldmeter_reading))

    def update_oldmeter(self, mileage):
        if mileage >=self.oldmeter_reading:
            self.oldmeter_reading = mileage
        else:
            print ("You can not roll back an oldmeter!")

    def increment_odometer(self, mileage):
        self.oldmeter_reading += mileage


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print ("This car has a {}-kwh battery.".format(self.battery_size))


my_tesla = ElectricCar('tesla', 'model s', '2019')


print (my_tesla.get_descriptive_name())
my_new_car = Car('audi', 'a4', 2019)
print (my_new_car.get_descriptive_name())

my_new_car.oldmeter_reading = 23
my_new_car.read_oldmeter()
"""文档字符串"""
