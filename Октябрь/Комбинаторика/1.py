import time


def main():
    alpha = ['Г', 'О', 'Д']

    count = 0
    for one in alpha:
        for two in alpha:
            for three in alpha:
                for four in alpha:
                    for five in alpha:
                        for six in alpha:
                            if one != 'О' and six != 'О':
                                count += 1
    print(count)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

