from fractions import Fraction
import math
#Fraction(math.pi).limit_denominator(100)
f=Fraction(math.pi).limit_denominator(100)
print("The fraction created is::",f)
print("Numerator::",f.numerator)