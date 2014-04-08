#!/usr/bin/env python3
import types

# decorator function for adding a free standing function
# to a specified class
def method(_class):
    def wrap(func):
        setattr(_class, func.__name__, types.MethodType(func, _class))
        def wrapped_f(*args, **kwargs):
            return func(*args, **kwargs)
        wrapped_f.__name__ = func.__name__
        return wrapped_f
    return wrap


def testMethodDecorator():
    class A:
        str = "helloWorld"

    @method(A)
    def removePrefix(self, prefix):
        if self.str.startswith(prefix):
            return self.str[len(prefix):]
        return self.str

    a = A()
    print(a.removePrefix("hello"))

if __name__ == '__main__':
    testMethodDecorator()