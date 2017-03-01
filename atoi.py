def demo_atoi(astr, base=10):
    """
    convert given string of numbers into integer. will check for invalid charcters
    will check if number should be negative
    :param astr: string of characters
    :param base: radix of number represented in string
    :return: int value of given string
    """
    sign = 1
    num = 0

    if astr[0] == '-':
        sign = -1
        astr = astr[1:]
    try:
        for c in astr:
            # loop through each char in string
            if base <= 10:
                if '0' <= c <= str(base-1):
                    num = num * base + ord(c) - ord('0')  # ord turns char into ascii value
                else:
                    raise ValueError('demo_atoi argument (%s) contains non-digit(s) for '
                                     'base %s' % (astr, base))
            elif 10 < base <= 16:
                if 'a' <= c <= chr(ord('a') + base - 11):
                    num = num * base + ord(c) - ord('a') + 10
                else:
                    raise ValueError('demo_atoi argument (%s) contains non-digit(s) for '
                                     'base %s' % (astr, base))
            else:
                print 'base out of range'
                #raise ValueError('demo_atoi argument (%s) contains non-digit(s)' % astr)
        print num * sign
        return num * sign

    except Exception as e:
        print e

'''
if -13465609 == demo_atoi('-1346 5609'):
    print True
else:
    print False
'''
demo_atoi('a', 16)
