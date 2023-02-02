file = open('1_file.txt').read()
rows = file.replace('A', ' ').replace('C', ' ').split()
print(max([len(row) for row in rows]))