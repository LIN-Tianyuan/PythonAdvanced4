def str_reverse(s):
    return s[::-1]

def substr(s, x, y):
    return s[x:y]

if __name__ == '__main__':
    str1 = str_reverse('abcd')
    print(str1)

    s = 'abcd'
    print(s[1:4])

    str2 = substr('abcd', 1, 4)
    print(str2)
