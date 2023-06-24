import inspect

def my_function(arg1, arg2, arg3):
    pass

num_args = len(inspect.signature(my_function).parameters)
print(num_args)  # Output: 3
