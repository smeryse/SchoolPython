file = open('4_file.txt').read()
rows = file.replace('L', ' ').replace('D', ' ').strip()
print(max([len(i) for i in rows]))