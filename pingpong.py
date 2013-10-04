# encoding: utf-8

def pingpong(n):
    """
    Should return the number passed
    >>> pingpong(1)
    1
    >>> pingpong(8)
    8

    Should return ping if number is multiple of 3
    >>> pingpong(3)
    'ping'
    >>> pingpong(9)
    'ping'

    Should return pong if number is multiple of 5
    >>> pingpong(5)
    'pong'
    >>> pingpong(50)
    'pong'

    Should return pingpong if number is multiple of 3 and 5
    >>> pingpong(60)
    'pingpong'
    >>> pingpong(90)
    'pingpong'

    >>> [pingpong(i) for i in range(1, 16)]
    [1, 2, 'ping', 4, 'pong', 'ping', 7, 8, 'ping', 'pong', 11, 'ping', 13, 14, 'pingpong']
    """
    _return = ""
    if (n % 3) == 0:
        _return += "ping"
    if (n % 5) == 0:
        _return += "pong"
    return _return or n



if __name__ == "__main__":
    import sys
    if 'test' in sys.argv:
        import doctest
        doctest.testmod()
    else:
        for i in xrange(1, 101):
            print pingpong(i)
