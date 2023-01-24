file = list(open('26-60.txt'))
K, N = map(lambda x: int(x), file[0][:-1].split())
spec_codes = {id: int(count[:-1]) for id, count in enumerate(file[1: K + 1])}
students = {data[:-1].split()[1]: data[:-1].split()[0] for data in file[K + 1:]}
print(students)