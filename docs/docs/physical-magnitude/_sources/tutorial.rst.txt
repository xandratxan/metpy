Tutorial
========

This tutorial is a good introduction on how to get started with ``physical-magnitude``.

.. contents:: Table of Contents

Installation
------------

``physical-magnitude`` can be installed in three different ways.

Install via pip from PyPi-like server:

.. code-block::

    pip install physical-magnitude --extra-index-url https://xandratxan.github.io/metpy/server/

Install via pip with GitHub repository url:

.. code-block::

    pip install git+https://github.com/xandratxan/physical-magnitude.git#egg=physical-magnitude

Clone GitHub repository and install via pip:

.. code-block::

 git clone git@github.com:xandratxan/physical-magnitude.git
 cd physical-magnitude
 pip install .

Operating with magnitudes
-------------------------

In this tutorial, we’ll show you step by step how to perform simple arithmetic operations with magnitudes,
including their values, uncertainties and units.

In a Python console, import the ``Magnitude`` class:

.. code-block::

    >>> from magnitude import Magnitude

Now define two magnitudes to operate with, including their values, uncertainties and units.
For example m1 = 100 ± 1 m (1%) and m2 = 200 ± 2 m (1%):

.. code-block::

    >>> m1 = m1 = Magnitude(value=100, unit='m', uncertainty=1)
    >>> m1
    100.0 ± 1.0 m (1.0%)
    >>> m2 = m2 = Magnitude(value=200, unit='m', uncertainty=2)
    >>> m2
    200.0 ± 2.0 m (1.0%)

Lets add these two magnitudes:

.. code-block::

    >>> m_sum = m1 + m2
    >>> m_sum
    300.0 ± 2.23606797749979 m (0.74535599249993%)

Lets subtract these two magnitudes:

.. code-block::

    >>> m_dif = m2 - m1
    >>> m_dif
    100.0 ± 2.23606797749979 m (2.23606797749979%)

Lets multiply these two magnitudes:

.. code-block::

    >>> m_prod = m1 * m2
    >>> m_prod
    20000.0 ± 282.842712474619 (m)·(m) (1.4142135623730951%)

Note that the unit of ``m_prod`` is ``(m)·(m)``, which is m².
Lest modify the unit of ``m_prod`` accordingly:

.. code-block::

    >>> m_prod.unit = 'm²'
    >>> m_prod
    20000.0 ± 282.842712474619 m² (1.4142135623730951%)

Lets divide these two magnitudes:

.. code-block::

    >>> m_div = m2 / m1
    >>> m_div
    2.0 ± 0.0282842712474619 (m)/(m) (1.4142135623730951%)

Note that the unit of ``m_div`` is ``(m)/(m)``, which means that the magnitude is non-dimensional.
Lest modify the unit of ``m_div`` accordingly:

.. code-block::

    >>> m_div.unit = ''
    >>> m_div
    2.0 ± 0.0282842712474619  (1.4142135623730951%)
