# (2*x^0)/1! + (3*x^2)/2! + (4*x^4)/3! + (5*x^6)/4! + (6*x^8)/5!......
def bereken(x, n):
    total = 0.0
    multiplier = 2.0
    power = x**0
    fac = 1.0
    
    for i in range(n):
        total += (multiplier * power) / fac
        
        multiplier += 1
        power *= x**2
        fac *= i+2
        
    return total
        