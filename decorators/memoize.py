#!/usr/bin/env python3

import collections
import functools


class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
      self.__name__ = func.__name__

   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)


if __name__ == '__main__':
   import time

   @memoized
   def fibonacci(n):
      "Return the nth fibonacci number."
      if n in (0, 1):
         return n
      return fibonacci(n-1) + fibonacci(n-2)

   def timeit(f, *args, **kwargs):
      time1 = time.time()
      ret = f(*args)
      time2 = time.time()
      print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
      return ret

   n = 150
   timeit(fibonacci, n)
   timeit(fibonacci, n)

