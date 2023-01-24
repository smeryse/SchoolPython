def f(n):
    lst = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.add(i)
            lst.add(n // i )
    return sorted(lst)


def main(n1=174457, n2=174505):
    result = []
    for i in range(n1, n2 + 1):
        if len(f(i)) == 4:
            result.append(i)

    print(len(result))

if __name__ == '__main__':
    main()