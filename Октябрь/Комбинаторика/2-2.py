import time, itertools


def main():
    string = 'МЕТРО'
    count = 0
    for one in string:
        for two in string:
            for three in string:
                for four in string:
                    if one != 'Р' and one != 'Т' and one != 'М' and four != 'Е' and four != 'О':
                        print(one, two, three, four, sep='')
                        count += 1
    print(count)


start_time = time.time()
main()
print(f"--- {time.time() - start_time} seconds ---")