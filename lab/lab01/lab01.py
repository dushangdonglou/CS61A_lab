def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    x = n
    if k > 0:
        for i in range(k-1):
            n -= 1
            x *= n
        return x
    else:
        return 1

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    x = 0
    for i in str(y):
        x += int(i)
    return x

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # 方法1
    # return str(n).count('88') != 0

    # 方法2
    # number = 0
    # while n > 0:
    #     if n % 10 == 8:
    #         number += 1
    #         if number == 2:
    #             return True
    #     else:
    #         number = 0
    #     n //= 10
    # return False

    # 方法3
    while n > 0:
        if n % 100 == 88:
            return True
        n //= 10
    return False




