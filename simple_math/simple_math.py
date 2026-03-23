"""
A collection of simple math operations.
"""

def simple_add(a,b):
    """The summation of two numbers.

    Parameters
    ----------
    a : int or float
        The first value to add.
    b : int or float
        The second value to add.

    Returns
    -------
    int or float
        The result of `a+b`.
    
    Examples
    --------
    >>> simple_add(1, 3)
    4
    >>> simple_add(5, 0)
    5
    """
    return a+b

def simple_sub(a,b):
    """The difference between two numbers.

    Parameters
    ----------
    a : int or float
        The value to be subtracted from.
    b : int or float
        The value to subtract.

    Returns
    -------
    int or float
        The result of `a - b`.
        
    Examples
    --------
    >>> simple_sub(7, 9)
    -2
    """
    return a-b

def simple_mult(a,b):
    """The product of two numbers.

    Parameters
    ----------
    a : int or float
        The first factor.
    b : int or float
        The second factor.

    Returns
    -------
    int or float
        The result of `a * b`.
    
    Examples
    --------
    >>> simple_mult(3, 4)
    12
    """
    return a*b

def simple_div(a,b):
    """The division of two numbers.

    Parameters
    ----------
    a : int or float
        The dividend.
    b : int or float
        The divisor.

    Returns
    -------
    int or float
        The result of `a * b`.
    
    Examples
    --------
    >>> simple_div(6, 3)
    2
    """
    return a/b

def poly_first(x, a0, a1):
    """Evaluate a first-order polynomial (linear function).
    
    Computes the result of f(x) = a0 + a1*x.
    

    Parameters
    ----------
    x : int or float
        The independent variable.
    a0 : int or float
        The constant term (intercept).
    a1 : int or float
        The coefficient of the first-order term (slope).

    Returns
    -------
    int or float
        The result of `a0 + a1 * x`.

    Examples
    --------
    >>> poly_first(2, 3, 4)
    11
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Evaluate a second-order polynomial (quadratic function).
    
    Computes the result of f(x) = a0 + a1*x + a2*x^2.

    Parameters
    ----------
    x : int or float
        The independent variable.
    a0 : int or float
        The constant term.
    a1 : int or float
        The coefficient of the first-order term.
    a2 : int or float
        The coefficient of the second-order term.

    Returns
    -------
    int or float
        The result of `a0 + a1 * x + a2 * x^2`.
    
    Examples
    --------
    >>> poly_first(2, 3, 4)
    23
    """
    return poly_first(x, a0, a1) + a2*(x**2)