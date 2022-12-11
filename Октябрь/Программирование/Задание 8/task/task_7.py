f = open('../file/17-257.txt')
lst = [int(i) for i in f]

k2 = [i for i in lst if i % 2 == 0]
nk2 = [i for i in lst if i % 2 != 0]

if max(k2) > max(nk2):
    print(
        len(k2),
        min(nk2),
        sep='\n'
    )