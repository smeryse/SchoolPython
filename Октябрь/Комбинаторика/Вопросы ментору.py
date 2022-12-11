from itertools import product

count = 0
for i in product('ДЕЙКСТРА', repeat=6):
    i = ''.join(i)
    f = i.find('Й')
    if f < len(i) - 1:
        if i[f + 1] != 'Е' and i[f + 1] != 'Й' and i[f + 1] != 'А':
            if i.count('Д') <= 1 and i.count('Е') <= 1 \
                    and i.count('Й') <= 1 and i.count('К') <= 1 \
                    and i.count('С') <= 1 and i.count('Т') <= 1 \
                    and i.count('Р') <= 1 and i.count('А') <= 1:
                count += 1
                print(i)

print(count)
