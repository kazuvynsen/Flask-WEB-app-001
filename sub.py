def wrapper_function(function):
    def inner_function():
        print('This is inner_function')
        function()

    return inner_function


@wrapper_function
def decorated_function():
    print('This is decorated function')


decorated_function()

# def add_function(n1, n2):
#     return n1 + n2
#
#
# def minus_function(n1, n2):
#     return n1 - n2
#
#
# def decorate_function(function, n1, n2):
#     return function(n1, n2)
#
#
# result_add = decorate_function(add_function, 1, 2)
# result_minus = decorate_function(minus_function, 1, 2)
#
# print(result_add)
# print(result_minus)

# --------------------------

# def outer_function():
#     print('This is outer_function')
#
#     def inner_function():
#         print("It's inner function")
#
#     return inner_function
#
#
# new_function = outer_function()
# new_function()

# -----------------------------
