#((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y)
lst = [0, 1]
print('x y z w')
for x in lst:
    for y in lst:
        for z in lst:
            for w in lst:
                f = ((x and w) or (w and x)) == ((z <= y) and (y <= x))
                if f == 1:
                    print(x, y, z, w)

