import cmath

#to find the phase angle
phi = cmath.phase(complex(-1.0, 1.0))
print(phi)

#to find the rectangular coordinates
c=cmath.rect(1,2)
print("real::",c.real)
print("imaginary::",c.imag)
print("complex number::",c)

#print the polar coordinates
p=cmath.polar(c)
print("polar::",p)
print(type(c))