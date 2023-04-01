How to guides
=============

This section describes how to accomplish common tasks with ``physical-magnitude``.

.. contents:: Table of Contents

How to define a magnitude
-------------------------

How to define a magnitude with uncertainty
..........................................

There are two options to define a magnitude with uncertainty:

- Provide the standard uncertainty of the magnitude.
- Provide the relative standard uncertainty of the magnitude.

If standard uncertainty is provided, for example d = 100 ± 1 m, relative standard uncertainty will be calculated:

.. code-block::

    >>> Magnitude(value=10, uncertainty=1, unit='m')
    100.0 ± 1.0 m (1.0%)

If relative standard uncertainty is provided, for example d = 100 m ± 1%, standard uncertainty will be calculated:

.. code-block::

    >>> Magnitude(value=100, uncertainty=0.01, unit='m', relative_uncertainty=True)
    100.0 ± 1.0 m (1.0%)

How to define a magnitude without uncertainty
.............................................

Magnitudes without uncertainties, for example d = 100 m, can be defined with zero uncertainty:

.. code-block::

    >>> Magnitude(value=100, uncertainty=0, unit='m')
    100.0 ± 0.0 m (0.0%)
    >>> Magnitude(value=100, uncertainty=0, unit='m', relative_uncertainty=True)
    100.0 ± 0.0 m (0.0%)

How to define a non-dimensional magnitude
.........................................

Non-dimensional magnitudes, for example d = 100 ± 1 (1%), can be defined with an empty string as unit:

.. code-block::

    >>> Magnitude(value=100, uncertainty=1, unit='')
    100.0 ± 1.0  (1.0%)

How to not define a magnitude
.............................

Magnitudes cannot be defined with negative uncertainties, since it has no physical meaning:

.. code-block::

    >>> Magnitude(value=10, uncertainty=-1, unit='m')
    ValueError: Uncertainty must be positive.

.. code-block::

    >>> Magnitude(value=100, uncertainty=-0.01, unit='m', relative_uncertainty=True)
    ValueError: Uncertainty must be positive.

How to operate with magnitudes
------------------------------

How to sum and subtract magnitudes
..................................

First, define some magnitudes to operate with them:

.. code-block::

    >>> m1 = Magnitude(value=100, unit='m', uncertainty=1)
    >>> m2 = Magnitude(value=200, unit='m', uncertainty=2)
    >>> m3 = Magnitude(value=200, unit='cm', uncertainty=2)

Magnitudes can be summed or subtracted as long as they have the same units:

.. code-block::

    >>> m1 + m2
    300.0 ± 2.23606797749979 m (0.74535599249993%)

.. code-block::

    >>> m2 - m1
    100.0 ± 2.23606797749979 m (2.23606797749979%)

If they have different units, an exception will be raised:

.. code-block::

    >>> m1 + m3
    TypeError: Added magnitudes must have the same units.

.. code-block::

    >>> m2 - m3
    TypeError: Subtracted magnitudes must have the same units.

How to multiply and divide magnitudes
.....................................

First, define some magnitudes to operate with them:

.. code-block::

    >>> m1 = Magnitude(value=100, unit='m', uncertainty=1)
    >>> m2 = Magnitude(value=200, unit='m', uncertainty=2)

Magnitudes can be multiplied or divided independently of their units.
The unit resulting from the product or the division will be the concatenation of the individual magnitudes:

.. code-block::

    >>> m1 * m2
    20000.0 ± 282.842712474619 (m)·(m) (1.4142135623730951%)

.. code-block::

    >>> m2 / m1
    2.0 ± 0.0282842712474619 (m)/(m) (1.4142135623730951%)

How to operate with more than two magnitudes
............................................

First, define some magnitudes to operate with them:

.. code-block::

    >>> m1 = Magnitude(value=100, unit='m', uncertainty=1)
    >>> m2 = Magnitude(value=200, unit='m', uncertainty=2)
    >>> m3 = Magnitude(value=200, unit='cm', uncertainty=2)
    >>> m4 = Magnitude(value=200, unit='m²', uncertainty=2)

Multiple magnitudes can be summed and/or subtracted as long as they have the same units:

.. code-block::

    >>> m1 + m2 + m1 - m2
    200.0 ± 3.1622776601683795 m (1.58113883008419%)

Multiple magnitudes can be multiplied and/or divided independently of their units:

.. code-block::

    >>> m1 * m2 / m3
    100.0 ± 1.7320508075688772 ((m)·(m))/(cm) (1.7320508075688772%)

Combining summation/subtraction with product/division require some unit management.
Trying to do ``m1 * m2 + m4`` will raise an error since the units of ``m1 * m2`` are ``'m·m'``
while the units of ``m4`` are ``'m²'``.

.. code-block::

    >>> m1 * m2 + m4
    TypeError: Added magnitudes must have the same units.

To work around this, first we need to define a new magnitude ``m`` as ``m1 * m2``:

.. code-block::

    >>> m = m1 * m2
    >>> m
    20000.0 ± 282.842712474619 (m)·(m) (1.4142135623730951%)

Then, we need to change the unit of ``m`` from ``'(m)·(m)'`` to ``'m²'``:

.. code-block::

    >>> m.unit = 'm²'
    >>> m
    20000.0 ± 282.842712474619 (m)·(m) (1.4142135623730951%)

Finally we can do ``m + m4``:

.. code-block::

    >>> m + m4
    20000.0 ± 282.842712474619 m² (1.4142135623730951%)
