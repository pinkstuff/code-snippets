#!/usr/bin/env python

class A(object):
    @classmethod
    def get_subclass_by_name(cls, name):
        try:
            return [c() for c in cls.__subclasses__() if c.__name__ == name][0]
        except IndexError:
            raise KeyError('%s is not a subclass of A' % name)

    def p(self):
        print "A"

class B(A):
    def p(self):
        print "B"

class C(A):
    def p(self):
        print "C"

class D(object):
    def p(self):
        print "D"

A.get_subclass_by_name('B').p()
A.get_subclass_by_name('C').p()
A.get_subclass_by_name('D').p()
