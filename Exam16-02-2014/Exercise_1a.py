class A:
    def __init__ (self, a_int):
        self.g = a_int
        self.b = None
    def add (self):
        self.g += 1
    
class B :
    def __init__ (self, a_int, an_a_obj):
        self.g = a_int
        self.a = an_a_obj
    def substract (self):
        self.g -= 1


a = A(5)
a2 = A(9)
b = B(21, a2)


def show (an_a_obj, a_b_obj):
    print '%d %d %d' % (an_a_obj.g, a_b_obj.g, a_b_obj.a.g)


show(a, b)
a.add()
show(a, b)
b.substract()
show(a, b)
b.a.add()
show(a, b)
a.b = b
show(a, a.b)
a.b.substract()
show(a, b)
b.a.b = a.b
show(b.a, a2.b)