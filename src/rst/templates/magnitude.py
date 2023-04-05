"""RST templates for physical-magnitude documentation."""


def api():
    """RST template for physical-magnitude package documentation API."""
    text = (
        f".. autoclass:: magnitude.magnitude.Magnitude\n"
        f"   :members:\n"
    )
    return text


def tutorial(import_package, str_m1, str_m2, m1, m2, m_sum, m_dif, m_prod1, m_prod2, m_div1, m_div2):
    """RST template for physical-magnitude package documentation tutorial.

    Parameters
    ----------
    import_package : str
        Statement to import Magnitude class.
    str_m1 : str
        Signature of m1 Magnitude object.
    str_m2 : str
        Signature of m2 Magnitude object.
    m1 : str
        Representation of m1 Magnitude object.
    m2 : str
        Representation of m2 Magnitude object.
    m_sum : str
        Representation of m1 + m2 Magnitude object.
    m_dif : str
        Representation of m2 - m1 Magnitude object.
    m_prod1 : str
        Representation of m1 * m2 Magnitude object.
    m_prod2 : str
        Representation of m1 * m2 Magnitude object with modified units.
    m_div1 : str
        Representation of m2 / m1 Magnitude object.
    m_div2 : str
        Representation of m2 / m1 Magnitude object with modified units.
    """
    text = (
        f"Operating with magnitudes\n"
        f"-------------------------\n"
        f"\n"
        f"In this tutorial, we’ll show you step by step how to perform simple arithmetic operations with magnitudes,\n"
        f"including their values, uncertainties and units.\n"
        f"\n"
        f"In a Python console, import the ``Magnitude`` class:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {import_package}\n"
        f"\n"
        f"Now define two magnitudes to operate with, including their values, uncertainties and units.\n"
        f"For example m1 = 100 ± 1 m (1%) and m2 = 200 ± 2 m (1%):\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 = {str_m1}\n"
        f"    >>> m1\n"
        f"    {m1}\n"
        f"    >>> m2 = {str_m2}\n"
        f"    >>> m2\n"
        f"    {m2}\n"
        f"\n"
        f"Lets add these two magnitudes:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_sum = m1 + m2\n"
        f"    >>> m_sum\n"
        f"    {m_sum}\n"
        f"\n"
        f"Lets subtract these two magnitudes:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_dif = m2 - m1\n"
        f"    >>> m_dif\n"
        f"    {m_dif}\n"
        f"\n"
        f"Lets multiply these two magnitudes:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_prod = m1 * m2\n"
        f"    >>> m_prod\n"
        f"    {m_prod1}\n"
        f"\n"
        f"Note that the unit of ``m_prod`` is ``(m·m)``, which is m².\n"
        f"Lest modify the unit of ``m_prod`` accordingly:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_prod.unit = 'm²'\n"
        f"    >>> m_prod\n"
        f"    {m_prod2}\n"
        f"\n"
        f"Lets divide these two magnitudes:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_div = m2 / m1\n"
        f"    >>> m_div\n"
        f"    {m_div1}\n"
        f"\n"
        f"Note that the unit of ``m_div`` is ``(m/m)``, which means that the magnitude is non-dimensional.\n"
        f"Lest modify the unit of ``m_div`` accordingly:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m_div.unit = ''\n"
        f"    >>> m_div\n"
        f"    {m_div2}\n"
        f""
    )
    return text


def howto(m1, str_m1, m2, str_m2, m3, str_m3, m4, str_m4, m5, str_m5, m6, str_m6, m7, str_m7,
          str_m8, str_m9, str_m10, str_m11, m_sum, m_dif, m_sum_exc, m_dif_exc, m_prod1, m_div1,
          m_multi_sum, m_multi_prod, m_multi_comb, m_multi_comb1, m_multi_comb2):
    """RST template for physical-magnitude package documentation tutorial.

    Parameters
    ----------
    m1 : str
        Representation of m1 Magnitude object.
    str_m1 : str
        Signature of m1 Magnitude object.
    m2 : str
        Representation of m2 Magnitude object.
    str_m2 : str
        Signature of m2 Magnitude object.
    m3 : str
        Representation of m3 Magnitude object.
    str_m3 : str
        Signature of m3 Magnitude object.
    m4 : str
        Representation of m4 Magnitude object.
    str_m4 : str
        Signature of m4 Magnitude object.
    m5 : str
        Representation of m5 Magnitude object.
    str_m5 : str
        Signature of m5 Magnitude object.
    m6 : str
        Representation of m6 Magnitude object.
    str_m6 : str
        Signature of m6 Magnitude object.
    m7 : str
        Representation of m7 Magnitude object.
    str_m7 : str
        Signature of m7 Magnitude object.
    str_m8 : str
        Signature of m8 Magnitude object.
    str_m9 : str
        Signature of m9 Magnitude object.
    str_m10 : str
        Signature of m10 Magnitude object.
    str_m11 : str
        Signature of m11 Magnitude object.
    m_sum : str
        Representation of m8 + m9 Magnitude object.
    m_sum_exc : str
        Representation of m8 + m10 Magnitude object with different units.
    m_dif : str
        Representation of m9 - m8 Magnitude object.
    m_dif_exc : str
        Representation of m9 - m10 Magnitude object with different units.
    m_prod1 : str
        Representation of m8 * m9 Magnitude object.
    m_div1 : str
        Representation of m9 / m8 Magnitude object.
    m_multi_sum : str
        Representation of m8 + m9 + m8 - m9 Magnitude object.
    m_multi_prod : str
        Representation of m8 * m9 / m10 Magnitude object.
    m_multi_comb : str
        Representation of m8 * m9 + m11 Magnitude object.
    m_multi_comb1 : str
        Representation of m8 * m9 Magnitude object.
    m_multi_comb2 : str
        Representation of m8 * m9 Magnitude object with changed units.
    """
    text = (
        f"How to define a magnitude\n"
        f"-------------------------\n"
        f"\n"
        f"How to define a magnitude with uncertainty\n"
        f"..........................................\n"
        f"\n"
        f"There are two options to define a magnitude with uncertainty:\n"
        f"\n"
        f"- Provide the standard uncertainty of the magnitude.\n"
        f"- Provide the relative standard uncertainty of the magnitude.\n"
        f"\n"
        f"If standard uncertainty is provided, for example d = 100 ± 1 m, "
        f"relative standard uncertainty will be calculated:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m1}\n"
        f"    {m1}\n"
        f"\n"
        f"If relative standard uncertainty is provided, for example d = 100 m ± 1%, "
        f"standard uncertainty will be calculated:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m2}\n"
        f"    {m2}\n"
        f"\n"
        f"How to define a magnitude without uncertainty\n"
        f".............................................\n"
        f"\n"
        f"Magnitudes without uncertainties, for example d = 100 m, can be defined with zero uncertainty:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m3}\n"
        f"    {m3}\n"
        f"    >>> {str_m4}\n"
        f"    {m4}\n"
        f"\n"
        f"How to define a non-dimensional magnitude\n"
        f".........................................\n"
        f"\n"
        f"Non-dimensional magnitudes, for example d = 100 ± 1 (1%), can be defined with an empty string as unit:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m5}\n"
        f"    {m5}\n"
        f"\n"
        f"How to not define a magnitude\n"
        f".............................\n"
        f"\n"
        f"Magnitudes cannot be defined with negative uncertainties, since it has no physical meaning:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m6}\n"
        f"    {m6}\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m7}\n"
        f"    {m7}\n"
        f"\n"
        f"How to operate with magnitudes\n"
        f"------------------------------\n"
        f"\n"
        f"How to sum and subtract magnitudes\n"
        f"..................................\n"
        f"\n"
        f"First, define some magnitudes to operate with them:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m8}\n"
        f"    >>> {str_m9}\n"
        f"    >>> {str_m10}\n"
        f"\n"
        f"Magnitudes can be summed or subtracted as long as they have the same units:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 + m2\n"
        f"    {m_sum}\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m2 - m1\n"
        f"    {m_dif}\n"
        f"\n"
        f"If they have different units, an exception will be raised:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 + m3\n"
        f"    {m_sum_exc}\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m2 - m3\n"
        f"    {m_dif_exc}\n"
        f"\n"
        f"How to multiply and divide magnitudes\n"
        f".....................................\n"
        f"\n"
        f"First, define some magnitudes to operate with them:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m8}\n"
        f"    >>> {str_m9}\n"
        f"\n"
        f"Magnitudes can be multiplied or divided independently of their units.\n"
        f"The unit resulting from the product or the division will be the concatenation of the individual magnitudes:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 * m2\n"
        f"    {m_prod1}\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m2 / m1\n"
        f"    {m_div1}\n"
        f"\n"
        f"How to operate with more than two magnitudes\n"
        f"............................................\n"
        f"\n"
        f"First, define some magnitudes to operate with them:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> {str_m8}\n"
        f"    >>> {str_m9}\n"
        f"    >>> {str_m10}\n"
        f"    >>> {str_m11}\n"
        f"\n"
        f"Multiple magnitudes can be summed and/or subtracted as long as they have the same units:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 + m2 + m1 - m2\n"
        f"    {m_multi_sum}\n"
        f"\n"
        f"Multiple magnitudes can be multiplied and/or divided independently of their units:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 * m2 / m3\n"
        f"    {m_multi_prod}\n"
        f"\n"
        f"Combining summation/subtraction with product/division require some unit management.\n"
        f"Trying to do ``m1 * m2 + m4`` will raise an error since the units of ``m1 * m2`` are ``'(m·m)'``\n"
        f"while the units of ``m4`` are ``'m²'``.\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m1 * m2 + m4\n"
        f"    {m_multi_comb}\n"
        f"\n"
        f"To work around this, first we need to define a new magnitude ``m`` as ``m1 * m2``:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m = m1 * m2\n"
        f"    >>> m\n"
        f"    {m_multi_comb1}\n"
        f"\n"
        f"Then, we need to change the unit of ``m`` from ``'(m·m)'`` to ``'m²'``:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m.unit = 'm²'\n"
        f"    >>> m\n"
        f"    {m_multi_comb2}\n"
        f"\n"
        f"Finally we can do ``m + m4``:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    >>> m + m4\n"
        f"    {m_multi_comb2}\n"
    )
    return text
