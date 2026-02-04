# A very basic backbone structure of a decorator function

def decorator_backbone(func):
   def logger(*args, **kwargs):
       # covering the body's details later
       pass
   return logger


# we could use it as follows
@decorator_backbone
def some_other_function(params):
    pass

# Another usage of the decorator exploiting the underlying concept of closures
def some_other_function1(params):
    pass

some_other_function1_decorated = decorator_backbone(some_other_function1)
some_other_function1_decorated()

