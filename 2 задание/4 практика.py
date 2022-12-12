# #Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z ) ∨ w.

# task_1
# print('x, y, w, z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = (x and (not(y))) or (y == z) or w
#                 if f == 0:
#                     print(str(x).ljust(2), str(y).ljust(2), str(w).ljust(2), str(z).ljust(2))

# task_2
# #(¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w.
# print('x, y, w, z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = ((not(x) and (not(y))) or (y == z) or (not(w)))
#                 if f == 0:
#                     for i in [x, y, w, z]:
#                         print(str(i).ljust(3), end='')
#                     print()

# task_3
# print('x y w z')
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 f = ((x <= y) == (y <= z)) and (y or w)
#                 if f == 1:
#                     print(x, y, w, z)
#
