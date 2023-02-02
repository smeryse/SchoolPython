file = open('2_file.txt').read()
rows = file.replace('A', ' ').replace('B', ' ').split()
print(max([len(row) for row in rows]))