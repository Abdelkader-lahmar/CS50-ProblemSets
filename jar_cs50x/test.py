def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

test = C()
print(test.f(2, -5))
print(test.__class__)
print(int.__class__)
