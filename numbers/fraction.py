from fractions import Fraction
#From two integers
Fraction(25, -100)
#From another fraction
Fraction(' -3/7 ')
#from a decimal
from decimal import Decimal
Fraction(Decimal('9.9'))
#from a decimal without quotes
from decimal import Decimal
Fraction(9.1)
#Empty Fraction
Fraction()