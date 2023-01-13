files = list(open('Files/1.txt'))
print(files)
counts = tuple(files[0].split())
files = sorted([int(file.replace('\n', '')) for file in files[1:]])
select = []
for file in files:
    if sum(select) + file < 8200:
        select.append(file)

print(len(select), max(select))