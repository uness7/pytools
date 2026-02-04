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
