def decorator_function(function):
    def wrapper_function():
        print("this function has been decorated")
        function()
        print("running it for a second time:")
        function()
        print("finishing decorating")
    return wrapper_function


@decorator_function
def say_hello():
    print("Hello")


say_hello()
