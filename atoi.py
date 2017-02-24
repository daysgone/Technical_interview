def demo_atoi(astr):
    num = 0
    for c in astr:
        # loop through each char in string
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - ord('0')
        else:
            raise ValueError('demo_atoi argument (%s) contains non-digit(s)' % astr)
    return num

print demo_atoi('134')
