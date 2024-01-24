#!/usr/bin/python3
def magic_calculation(a, b):
    function = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                function += a ** b / i
        except Exception:
            function = b + a
    return (function)
