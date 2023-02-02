f = open('3_file.txt').read()
count = 1
counts = []
for i in range(len(f) - 1):
    if f[i] != f[i + 1] and f[i] != 'C' and f[i + 1] != 'C':
        count += 1
    else:
        counts.append(count)
        count = 1

print(max(counts))