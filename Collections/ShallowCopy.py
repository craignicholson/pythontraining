def shallow_copy():

    a = [[1,2],[3,4]]
    b = a[:]

    print(id(a))
    print(id(2))
    print(a is b)
    print(a == b)
    print(a[0] is b[0])
    a[0] = [8,9]
    print(a)
    print(b)
    a[1].append(5)
    # a 1 and b 1 referer to the same inner list so it changes both
    print(a)
    print(b)

    # another example with repetition
    s = [[-1,1]] * 5
    print(s)
    s[3].append(7)
    print(s)


def main():
    shallow_copy()


if __name__ == '__main__':
    main()
