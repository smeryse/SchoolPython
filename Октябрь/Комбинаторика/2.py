import time, itertools


def main():
    string = 'МЕТРО'
    count = 0
    for i in itertools.product(string, repeat=4):
        if i[0] != 'Р' and i[0] != 'Т' and i[0] != 'М' and i[-1] != 'Е' and i[-1] != 'О':
            print(*i, sep='')
            count += 1
    print(count)


start_time = time.time()
main()
print(f"--- {time.time() - start_time} seconds ---")