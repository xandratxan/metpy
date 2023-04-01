# Code for physical-magnitude package documentation

from magnitude import Magnitude

# How to define magnitudes

# How to define a magnitude with uncertainty
m1 = Magnitude(value=100, uncertainty=1, unit='m')
str_m1 = "Magnitude(value=100, uncertainty=1, unit='m')"

# How to define a magnitude with relative uncertainty
m2 = Magnitude(value=100, uncertainty=0.01, unit='m', relative_uncertainty=True)
str_m2 = "Magnitude(value=100, uncertainty=0.01, unit='m', relative_uncertainty=True)"

# How to define a magnitude with no uncertainty
m3 = Magnitude(value=100, uncertainty=0, unit='m')
str_m3 = "Magnitude(value=100, uncertainty=0, unit='m')"
m4 = Magnitude(value=100, uncertainty=0, unit='m', relative_uncertainty=True)
str_m4 = "Magnitude(value=100, uncertainty=0, unit='m', relative_uncertainty=True)"

# How to define a non-dimensional magnitude
m5 = Magnitude(value=100, uncertainty=1, unit='')
str_m5 = "Magnitude(value=100, uncertainty=1, unit='')"

# How to not define a magnitude, negative uncertainty
try:
    m6 = Magnitude(value=100, uncertainty=-1, unit='m')
except ValueError as exc:
    m6 = f'ValueError: {exc}'
str_m6 = "Magnitude(value=100, uncertainty=-1, unit='m')"
try:
    m7 = Magnitude(value=100, uncertainty=-0.01, unit='m', relative_uncertainty=True)
except ValueError as exc:
    m7 = f'ValueError: {exc}'
str_m7 = "Magnitude(value=100, uncertainty=-0.01, unit='m', relative_uncertainty=True)"

# How to operate with magnitudes

m8 = Magnitude(value=100, unit='m', uncertainty=1)
str_m8 = "m1 = Magnitude(value=100, unit='m', uncertainty=1)"
m9 = Magnitude(value=200, unit='m', uncertainty=2)
str_m9 = "m2 = Magnitude(value=200, unit='m', uncertainty=2)"
m10 = Magnitude(value=200, unit='cm', uncertainty=2)
str_m10 = "m3 = Magnitude(value=200, unit='cm', uncertainty=2)"
m11 = Magnitude(value=200, unit='m²', uncertainty=2)
str_m11 = "m4 = Magnitude(value=200, unit='m²', uncertainty=2)"

# How to sum and subtract magnitudes
m_sum = m8 + m9
m_dif = m9 - m8
try:
    m_sum_exc = m8 + m10
except TypeError as exc:
    m_sum_exc = f'TypeError: {exc}'
try:
    m_dif_exc = m9 - m10
except TypeError as exc:
    m_dif_exc = f'TypeError: {exc}'

# How to multiply magnitudes
m_prod1 = m8 * m9
m_prod2 = m8 * m9
m_prod2.unit = 'm²'

# How to divide magnitudes
m_div1 = m9 / m8
m_div2 = m9 / m8
m_div2.unit = ''

# How to operate with more than two magnitudes
m_multi_sum = m8 + m9 + m8 - m9
m_multi_prod = m8 * m9 / m10
try:
    m_multi_comb = m8 * m9 + m11
except TypeError as exc:
    m_multi_comb = f'TypeError: {exc}'
m_multi_comb1 = m8 * m9
m_multi_comb2 = m8 * m9
m_multi_comb2.unit = 'm²'
m_multi_comb3 = m_multi_comb2 + m11
