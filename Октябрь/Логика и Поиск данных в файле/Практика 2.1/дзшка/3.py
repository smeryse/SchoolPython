#((x → y) ≡ (y → z)) ∧ (y ∨ w).

print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (((x <= y) == (y <= z)) and (y or w))
                if f == 1:
                    print(x, y, z, w)

