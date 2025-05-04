# firstName = input("Enter Your First Name - ")
# lastName = input("Enter your last Name - ")
# age = int(input("Enter Your Age - "))
# print(f"My Name is {firstName} {lastName} and I am {age} years old!")

# num1, num2, num3 = map(int, input("Enter 3 numbers - ").strip().split(" "))
# print(num1, num2, num3)
# # print(type(num1), type(num2), type(num3))
#
# amount = 107.2523
# print("The amount is ${:.2f}".format(amount))

#
# def add_numbers(*args):
#     for arg in args:
#         print(arg, end=' ')
#
#
# def show_details(**kwargs):
#     for k, arg in kwargs.items():
#         print(f"{k} - {arg}")
#
#
# show_details(name="Aaroh Sinha", occupation="Student and Programmer", age=19)


# n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
#
#
# print(n(12))
#
# aboutPlayer = "His name is {} and he is a {}".format(input("Enter Name - "), input("Enter role - "))
# print(aboutPlayer)
#
# dict1 = {
#     "name": "Aaroh Sinha",
#     "age": 19,
#     "location": "India",
#     "occupation": "Programmer"
# }
#
# print(dict1)
# print(list(dict1.keys()))
# print(list(dict1.items()))
# print(list(dict1.values()))
# print(dict1["name"])
# print(dict1.get("location"))

# # Aaroh 95 92 88 Mehul 90 86 93 Tanvi 99 91 85
# name1, m1, m2, m3, name2, m4, m5, m6, name3, m7, m8, m9 = input("Enter names and marks - ").strip().split(" ")
# marks = {
#     name1: (m1, m2, m3),
#     name2: (m4, m5, m6),
#     name3: (m7, m8, m9)
# }
# print(marks)
# del marks["Tanvi"]
# print(marks)
# marks.clear()
# print(marks)


# students = [
#     {'name': 'Aaroh', 'maths': 95, 'physics': 91},
#     {'name': 'Mehul', 'maths': 88, 'physics': 93},
#     {'name': 'Tanvi', 'maths': 99, 'physics': 85}
# ]
# students_sorted = sorted(students, key=lambda x: x["physics"])
# print(students_sorted)


# def greet(fx):
#     def mfx():
#         print("GoodMorning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
#
#
# @greet
# def hello():
#     print("Hello World")
#
#
# hello()

# def decorator(fn):
#     def show(*args, **kwargs):
#         print("HEY THIS IS THE STARTING")
#         fn(*args, **kwargs)
#         print("HEY IT HAS ENDED")
#     return show
#
#
# @decorator
# def print_primes(n):
#     for i in range(2, n + 1):
#         is_prime = False
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 is_prime = True
#                 break
#         if not is_prime:
#             print(i)
#
# print_primes(100)

try:
    n = 10
    res = 100 / n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print("Result is", res)
finally:
    print("Execution complete.")


