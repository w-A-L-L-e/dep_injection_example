# Authoer: Walter Schreppers
# MRO and super (method resolution order) testing in practice
class Parent:
    def __init__(self):
        print("init of class Parent")

    def f(self):
        print("method f on Parent")
        # super().f()  # this would call super on 'object' but that does not exist

class A(Parent):
    def __init__(self):
        print("init of class A")

    def f(self):
        print("method f on A")
        super().f()

class B(Parent):
    def __init__(self):
        print("init of class B")

    def f(self):
        print("method f on B")
        super().f()


class C(A,B):
    def __init__(self):
        print("init of class C")

    def f(self):
        print("method f on C")
        super().f()


if __name__ == '__main__':
    ctest = C()
    ctest.f()

