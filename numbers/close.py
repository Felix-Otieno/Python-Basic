import math#checking whether it is a number or not
#compare the closeness of two values
print("with absolute tolerance  difference::", math.isclose(1.5, 2.05, abs_tol = 0.55))

print("with relative difference < difference::", math.isclose(1.5,1.75,rel_tol=0.5))