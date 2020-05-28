class A:
    def f(self):
        print('A')

class AA(A):
    def f(self):
        print('AA')
        super(AA, self).f()

class AB(A):
    def f(self):
        print('AB')
        super(AB, self).f()

class C(AA, AB):
    def f(self):
        print('C')
        super(C, self).f()
        # AB.f(self)


c = C()
c.f()