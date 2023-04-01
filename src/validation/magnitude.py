from math import sqrt

from magnitude import Magnitude


def check_magnitude_definition(magnitude_, value_, uncertainty_, relative_uncertainty_, unit_, message_):
    print(message_)
    print(f'Value: {value_} == {magnitude_.value}')
    print(f'Uncertainty: {uncertainty_} == {magnitude_.uncertainty}')
    print(f'Relative uncertainty: {relative_uncertainty_} == {magnitude_.relative_uncertainty}')
    print(f'Unit: {unit_} == {magnitude_.unit}')
    assert value_ == magnitude_.value
    assert uncertainty_ == magnitude_.uncertainty
    assert relative_uncertainty_ == magnitude_.relative_uncertainty()
    assert unit_ == magnitude_.unit
    print()


# 1. How to define magnitudes

# How to define a magnitude with uncertainty

message = 'How to define a magnitude with uncertainty'
value, uncertainty, unit = 20, 2, 'm'
relative_uncertainty = uncertainty / value
magnitude = Magnitude(value=20, uncertainty=2, unit='m')
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

message = 'How to define a magnitude with relative uncertainty'
value, relative_uncertainty, unit = 20, 0.1, 'm'
uncertainty = value * relative_uncertainty
magnitude = Magnitude(value=20, uncertainty=0.1, unit='m', relative_uncertainty=True)
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# How to define a magnitude with zero uncertainty

message = 'How to define a magnitude without uncertainty'
value, uncertainty, unit = 20, 0, 'm'
relative_uncertainty = uncertainty / value
magnitude = Magnitude(value=20, uncertainty=0, unit='m')
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

message = 'How to define a magnitude without uncertainty'
value, relative_uncertainty, unit = 20, 0, 'm'
uncertainty = value * relative_uncertainty
magnitude = Magnitude(value=20, uncertainty=0, unit='m', relative_uncertainty=True)
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# How to define a non-dimensional magnitude

message = 'How to define a non-dimensional magnitude'
value, uncertainty, unit = 20, 2, ''
relative_uncertainty = uncertainty / value
magnitude = Magnitude(value=20, uncertainty=2, unit='')
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# 2. How to operate with magnitudes

value1, uncertainty1, unit1 = 10, 1, 'm'
value2, uncertainty2, unit2 = 20, 2, 'm'
relative_uncertainty1 = uncertainty1 / value1
relative_uncertainty2 = uncertainty2 / value2
m1 = Magnitude(value=10, uncertainty=1, unit='m')
m2 = Magnitude(value=20, uncertainty=2, unit='m')

# How to sum magnitudes
message = 'How to sum magnitudes'
value = value1 + value2
uncertainty = sqrt(uncertainty1 ** 2 + uncertainty2 ** 2)
relative_uncertainty = uncertainty / value
unit = 'm'
magnitude = m1 + m2
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# How to subtract magnitudes
message = 'How to subtract magnitudes'
value = value2 - value1
uncertainty = sqrt(uncertainty1 ** 2 + uncertainty2 ** 2)
relative_uncertainty = uncertainty / value
unit = 'm'
magnitude = m2 - m1
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# How to multiply magnitudes
message = 'How to multiply magnitudes'
value = value1 * value2
relative_uncertainty = sqrt(relative_uncertainty1 ** 2 + relative_uncertainty2 ** 2)
uncertainty = value * relative_uncertainty
unit = '(m)·(m)'
magnitude = m1 * m2
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)

# How to divide magnitudes
message = 'How to divide magnitudes'
value = value2 / value1
relative_uncertainty = sqrt(relative_uncertainty1 ** 2 + relative_uncertainty2 ** 2)
uncertainty = value * relative_uncertainty
unit = '(m)/(m)'
magnitude = m2 / m1
check_magnitude_definition(magnitude, value, uncertainty, relative_uncertainty, unit, message)
