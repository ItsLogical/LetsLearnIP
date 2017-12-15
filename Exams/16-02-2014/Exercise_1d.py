e = -3
f = 7

def show (x, y):
    print '%d %d' % (x, y)
    
def method_a (d, e):
    global f
    d = e + f
    e = d + f
    f = d / e
    show(e, f)
    return d

def method_b (f):
    global e
    d = method_a(f, e)
    show(d, f)
    e += d
    f -= 3
    return e-f

e = method_a(e, f)
show(e, f)
f = method_b(f)
show(e, f)