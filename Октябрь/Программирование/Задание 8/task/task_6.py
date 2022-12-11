f = open('../file/17-257.txt')
lst = [int(i) for i in f]

a, b = [], []

for i in lst:
    if i % 11 == 0:
        a.append(i)
    if i % 17 == 0:
        b.append(i)

if len(a) > len(b):
    print(len(a),
          min(a),
          sep='\n'
          )
else:
    print(len(b),
          min(b),
          sep='\n'
          )