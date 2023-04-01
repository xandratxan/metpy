Tutorial
========

This tutorial is a good introduction in how to get started with ``physical-magnitude``.

Installation
------------

``physical-magnitude`` can be installed in three different ways.

Install via pip from PyPi-like server:

.. code-block::

    pip install physical-magnitude --extra-index-url https://xandratxan.github.io/python-package-server/

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
For example m1 = 10 ± 1 m (10%) and m2 = 20 ± 2 m (10%):

.. code-block::

    >>> m1 = m1 = Magnitude(value=10, uncertainty=1, unit='m')
    >>> m1
    10.0 ± 1.0 m (10.0%)
    >>> m2 = m2 = Magnitude(value=20, uncertainty=2, unit='m')
    >>> m2
    20.0 ± 2.0 m (10.0%)

Lets add these two magnitudes:

.. code-block::

    >>> m_sum = m1 + m2
    >>> m_sum
    30.0 ± 2.23606797749979 m (7.4535599249993%)

Lets subtract these two magnitudes:

.. code-block::

    >>> m_dif = m2 - m1
    >>> m_dif
    10.0 ± 2.23606797749979 m (22.360679774997898%)

Lets multiply these two magnitudes:

  .. code-block::

    >>> m_prod = m1 * m2
    >>> m_prod
    200.0 ± 28.284271247461906 (m)·(m) (14.142135623730953%)

Note that the unit of ``m_prod`` is ``(m)·(m)``, which is m².
Lest modify the unit of ``m_prod`` accordingly:

  .. code-block::

    >>> m_prod.unit = 'm²'
    >>> m_prod
    200.0 ± 28.284271247461906 m² (14.142135623730953%)

Lets divide these two magnitudes:

  .. code-block::

    >>> m_div = m2 / m1
    >>> m_div
    2.0 ± 0.28284271247461906 (m)/(m) (14.142135623730953%)

Note that the unit of ``m_div`` is ``(m)/(m)``, which means that the magnitude ``m_div`` is non-dimensional.
Lest modify the unit of ``m_div`` accordingly:

.. code-block::

    >>> m_div.unit = ''
    >>> m_div
    2.0 ± 0.28284271247461906  (14.142135623730953%)
